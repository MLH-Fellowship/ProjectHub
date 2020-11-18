import jwt
from backend.github_auth import request_access_token
from settings import PRIV_KEY_PATH
from backend.generate_keys import load_public_key, load_private_key

"""
Authentication Flow:
1. User presses login, signs into GitHub, which returns us a code.
2. We send the code, client_id, and client_secret via our backend to GitHub, which returns an access_code.
3. We take the access_code, put it inside a dict, and put it into a JWT. Then we encrypt it via our keys and send it via
   our internal API to the front-end.
4. When we want to make an authenticated call for a user, the JWT is sent to the server, where it is decrypted via
   with the public key.
5. We then use that decrypted access token to make a call to the GitHub API.
"""


def encode_jwt(data, private_key_path):
    private_key = load_private_key(private_key_path)
    payload = {"access_token": data}
    encoded = jwt.encode(payload=payload, key=private_key, algorithm="RS256")
    return encoded


def decode_jwt(data, public_key_path):
    public_key = load_public_key(public_key_path)
    try:
        decoded = jwt.decode(jwt=data, key=public_key, algorithms="RS256")
        return decoded
    except ValueError:
        # We want to reject the token and require the user to sign in again
        return None

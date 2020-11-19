import jwt
from generate_keys import load_public_key, load_private_key


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

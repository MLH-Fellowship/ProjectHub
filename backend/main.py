from fastapi import FastAPI
from starlette import status
from pydantic import BaseModel
from handle_tokens import decode_jwt, encode_jwt
from github_auth import request_access_token
from settings import PRIV_KEY_PATH, PUB_KEY_PATH

app = FastAPI()


class Token(BaseModel):
    encoded_jwt: str


@app.get("/")
def read_root():
    return "Alrighty then"


@app.get("/auth/{code}")
def return_jwt(code):
    at = request_access_token(code)
    if at == "Invalid Request":
        return at, status.HTTP_403_FORBIDDEN
    else:
        print(PRIV_KEY_PATH)
        encoded = encode_jwt(at, PRIV_KEY_PATH)
        return {"token": encoded}


@app.post("/teams")
def teams(jwt: Token, user):
    # Decode and verify the jwt
    try:
        decoded = decode_jwt(jwt.encoded_jwt, PUB_KEY_PATH)
        return decoded, user
    except ValueError:
        return status.HTTP_403_FORBIDDEN

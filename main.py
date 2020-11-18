from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from backend.handle_tokens import decode_jwt, encode_jwt
from backend.github_auth import request_access_token
from settings import PRIV_KEY_PATH, PUB_KEY_PATH
from backend.generate_keys import read_public_key
from starlette.testclient import TestClient
from fastapi.encoders import jsonable_encoder

app = FastAPI()


class Item(BaseModel):
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
        return encoded

@app.post("/token/")
def create_item(jwt: Item):
    # Decode and verify the jwt, call Github auth,
    try:
        decoded = decode_jwt(jwt, PUB_KEY_PATH)
    except ValueError:
        return status.HTTP_403_FORBIDDEN


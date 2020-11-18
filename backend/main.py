from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from backend.handle_tokens import decode_jwt
from backend.generate_keys import read_public_key

app = FastAPI()


class Item(BaseModel):
    jwt: dict


@app.get("/")
def read_root():
    return "Alrighty then"

@app.get("/token", status_code=200)
def create_item(jwt: Item, response: Response):
    decoded = decode_jwt(jwt, read_public_key("test.pub"))
    if decoded is None:
        response.status_code = status.HTTP_403_FORBIDDEN
        return response.status_code
    else:
        response.status_code = status.HTTP_200_OK
        return {"status": response.status_code,
                "payload": decoded}


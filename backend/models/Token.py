from pydantic import BaseModel


class Token(BaseModel):
    encoded_jwt: str
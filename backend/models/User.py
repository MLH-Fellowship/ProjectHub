from pydantic import BaseModel


class User(BaseModel):
    username: str   # TODO: remove and take from cookies or api
    name: str       # TODO: remove and take from cookies or api
    timezone_offset: int
    bio: str
    skills: list[str]
    interests: list[str]
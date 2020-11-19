from pydantic import BaseModel


class User(BaseModel):
    username: str
    name: str
    timezone_offset: int
    bio: str
    skills: list[str]
    interests: list[str]
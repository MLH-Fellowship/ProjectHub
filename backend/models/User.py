from pydantic import BaseModel


class User(BaseModel):
    username: str
    name: str
    timezone: int
    bio: str
    skills: list[str]
    interests: list[str]
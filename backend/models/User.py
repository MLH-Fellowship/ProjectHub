from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    login: Optional[str]
    name: Optional[str]
    timezone_offset: int
    bio: str
    skills: List[str]
    interests: List[str]
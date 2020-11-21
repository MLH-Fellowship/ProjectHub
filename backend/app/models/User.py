from typing import List, Optional
from pydantic import BaseModel


class MicroUser(BaseModel):
    login: str
    name: str
    bio: str
    html_url: str = ''
    avatar_url: str = ''


class User(BaseModel):
    id: Optional[int]
    login: Optional[str]
    name: Optional[str]
    timezone_offset: int
    bio: str
    skills: List[str]
    interests: List[str]
    pods: List[str]
    projects: Optional[List[str]]

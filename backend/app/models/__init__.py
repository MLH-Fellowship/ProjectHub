from typing import List, Optional
from pydantic import BaseModel


class MicroUser(BaseModel):
    login: str
    name: str
    avatar: str
    github: str
    bio: str
    pods: List[str]
    html_url: str = ''
    avatar_url: str = ''


class Project(BaseModel):
    id: Optional[int]
    owner: Optional[int]
    slug: Optional[str]
    name: str
    description: str
    source: str
    demo: str
    tags: List[str]
    languages: List[str]
    user: Optional[MicroUser]
    state: Optional[str]


class ExplorePage(BaseModel):
    projects: list[Project]
    pods: List[str] = [] # shared memory but it should never be set, only replaced
    languages: List[str]    


class User(BaseModel):
    id: Optional[int]
    login: Optional[str]
    name: Optional[str]
    github: Optional[str]
    avatar: Optional[str]
    timezone_offset: int
    bio: str
    skills: List[str]
    interests: List[str]
    pods: List[str]
    explorer: Optional[List[ExplorePage]]

from typing import Optional, List
from pydantic import BaseModel

from app.models.User import MicroUser


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
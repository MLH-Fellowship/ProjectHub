from typing import Optional
from pydantic import BaseModel


class Project(BaseModel):
    id: Optional[int]
    owner: Optional[int]
    name: str
    description: str
    source: str
    demo: str
    tags: list[str]

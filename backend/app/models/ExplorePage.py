from typing import List
from pydantic import BaseModel

from app.models.Project import Project


class ExplorePage(BaseModel):
    projects: list[Project]
    pods: List[str]
    languages: List[str]
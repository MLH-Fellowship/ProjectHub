from pydantic import BaseModel


class Project(BaseModel):
    name: str
    description: str
    source_link: str
    demo_link: str
    images: str
    tags: list[str]
    authors: list[str]
    id: str
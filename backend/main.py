from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    access_token: str


@app.get("/")
def read_root():
    return "Alrighty then"

@app.post("/user")
def create_item(item: Item):
    # Placeholder for an actual system
    return item
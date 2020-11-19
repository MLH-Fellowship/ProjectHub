from fastapi import FastAPI
from starlette import status
from pydantic import BaseModel
from handle_tokens import decode_jwt, encode_jwt
from github_auth import request_access_token, GH
from settings import PRIV_KEY_PATH, PUB_KEY_PATH
<<<<<<< HEAD
from db_connect import Insert, Update
=======
from db_connect import Insert
>>>>>>> c4fe398d2c4e0c62bf075fdf4d49d72b792b4203

app = FastAPI()


class Token(BaseModel):
    encoded_jwt: str


class Project(BaseModel):
    name: str
    description: str
    source_link: str
    demo_link: str
    images: str
    tags: list
    authors: list
<<<<<<< HEAD
    id: str
=======
>>>>>>> c4fe398d2c4e0c62bf075fdf4d49d72b792b4203


class User(BaseModel):
    username: str
    name: str
    timezone: int
    bio: str
    skills: list
    interests: list


@app.get("/auth/{code}")
def return_jwt(code):
    at = request_access_token(code)
    auth = GH(at=at)
    meta = auth.meta()

    if at == "Invalid Request":
        return status.HTTP_403_FORBIDDEN
    else:
        encoded = encode_jwt(at, PRIV_KEY_PATH)
        return {"token": encoded, "meta": meta}


@app.post("/teams")
def teams(jwt: Token):
    # Decode and verify the jwt
    try:
        decoded = decode_jwt(jwt.encoded_jwt, PUB_KEY_PATH)
        return decoded
    except ValueError:
        return status.HTTP_403_FORBIDDEN


@app.post("/projects")
def insert_project(json: Project):
<<<<<<< HEAD
    if Update().project_exists(json=json):
        Update().update_project(json=json)
    else:
        Insert().insert_project(json=json)
=======
    Insert().insert_project(json=json)
>>>>>>> c4fe398d2c4e0c62bf075fdf4d49d72b792b4203


@app.get("/projects")
def query_projects(pod: str = "", tags: str = ""):
    # query based on filters given
    pass


@app.get("/projects/{project}")
def query_project(project):
    # query specific project id
    pass


@app.post("/user/{user}")
def insert_user(json: User):
<<<<<<< HEAD
    if Update().user_exists(json=json):
        Update().update_user(json=json)
    else:
        Insert().insert_user(json)

=======
    Insert().insert_user(json)
>>>>>>> c4fe398d2c4e0c62bf075fdf4d49d72b792b4203


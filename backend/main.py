from fastapi import FastAPI
from starlette import status
from utils import jwe
from github_auth import request_access_token, GitHub
import utils.database as db
from apiparse import parse_project_query, parse_user_query
from models import Token, Project, User

app = FastAPI()


@app.get("/auth/{code}")
def return_jwt(code):
    auth = GitHub.from_code(code)
    meta = auth.meta()

    if auth.access_token == "Invalid Request":
        return status.HTTP_403_FORBIDDEN
    else:
        encoded = jwe.encode(auth.access_token)
        return {"token": encoded, "meta": meta}


@app.post("/teams")
def teams(jwt: Token):
    # Decode and verify the jwt
    try:
        decoded = jwe.decode(jwt.encoded_jwt)
        return decoded
    except ValueError:
        return status.HTTP_403_FORBIDDEN


@app.post("/projects")
def insert_project(json: Project):
    update = db.Update(json=json)
    if update.project_exists():
        update.update_project()
    else:
        db.Insert().insert_project(json=json)


@app.get("/projects/{project}")
def query_project(project):
    # query specific project id
    q = db.Query().query_projects(project=project)
    parsed = parse_project_query(q)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed


@app.post("/user/{user}")
def insert_user(json: User):
    update = db.Update(json=json)
    if update.user_exists():
        update.update_user()
    else:
        db.Insert().insert_user(json)


@app.get("/user/{username}")
def query_user(username):
    query = db.Query().query_users(username)
    parsed = parse_user_query(query)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed

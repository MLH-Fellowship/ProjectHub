from fastapi import FastAPI
from starlette import status
from utils import jwe
from github_auth import request_access_token, GH
from db_connect import Insert, Update, Query
from apiparse import parse_project_query, parse_user_query
from models import Token, Project, User

app = FastAPI()


@app.get("/auth/{code}")
def return_jwt(code):
    at = request_access_token(code)
    auth = GH(at=at)
    meta = auth.meta()

    if at == "Invalid Request":
        return status.HTTP_403_FORBIDDEN
    else:
        encoded = jwe.encode(at)
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
    update = Update(json=json)
    if update.project_exists():
        update.update_project()
    else:
        Insert().insert_project(json=json)


@app.get("/projects/{project}")
def query_project(project):
    # query specific project id
    q = Query().query_projects(project=project)
    parsed = parse_project_query(q)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed


@app.post("/user/{user}")
def insert_user(json: User):
    update = Update(json=json)
    if update.user_exists():
        update.update_user()
    else:
        Insert().insert_user(json)


@app.get("/user/{username}")
def query_user(username):
    query = Query().query_users(username)
    parsed = parse_user_query(query)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed

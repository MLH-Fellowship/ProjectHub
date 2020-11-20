from fastapi import FastAPI, Depends
from starlette import status
from utils import jwe
from github_auth import GitHub
import utils.database as db
from apiparse import parse_project_query, parse_user_query
from models import Token, Project, User
from utils.jwe import HTTPBearerJWEScheme

app = FastAPI()

http_bearer_scheme = HTTPBearerJWEScheme()


@app.get("/login/github/{code}")
def login_via_gitub(code):
    auth = GitHub.from_code(code)

    if auth.access_token == "Invalid Request":
        return status.HTTP_403_FORBIDDEN
    else:
        meta = auth.meta()
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
    if db.exists.project(json):
        db.update.project(json)
    else:
        db.insert.project(json)


@app.get("/projects/{project}")
def query_project(project):
    # query specific project id
    q = db.query.projects(project)
    parsed = parse_project_query(q)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed


@app.post("/user")
def insert_user(user: User, token: str = Depends(http_bearer_scheme)):
    # TODO: look up user by github_id in token not info passed in json
    if db.exists.user(user):
        db.update.user(user)
    else:
        db.insert.user(user)


@app.get("/user/{username}")
def query_user(username):
    query = db.query.users(username)
    parsed = parse_user_query(query)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed

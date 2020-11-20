from fastapi import FastAPI, Depends
from starlette import status
from utils import jwe
from utils.github import GitHub
import utils.database as db
from apiparse import parse_project_query, parse_user_query
from models import Project, User
from utils.jwe import HTTPBearerJWEScheme, HTTPAuthorizationJWT

app = FastAPI()
http_bearer_scheme = HTTPBearerJWEScheme()


@app.get("/login/github/{code}")
def login_via_gitub(code):
    auth = GitHub.from_code(code)

    if auth.access_token == "Invalid Request":
        return status.HTTP_403_FORBIDDEN
    else:
        encoded = jwe.encode(auth.user.id, auth.access_token)
        return {
            "token": encoded,
            "meta": auth.get_meta_dict(),
            "onBoarding": not db.exists.user(auth.user.id)
        }


@app.post("/project")
def new_project(json: Project, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if db.exists.project(json):
        db.update.project(json)
    else:
        db.insert.project(json)


@app.put("/project")
def update_project(json: Project, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if db.exists.project(json):
        db.update.project(json)
    else:
       return status.HTTP_400_BAD_REQUEST


@app.get("/project/{project_id}")
def get_project(project_id):
    # query specific project id
    q = db.query.projects(project_id)
    parsed = parse_project_query(q)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed


@app.get("/projects")
def get_project(project_id):
    # TODO: list all projects
    # query specific project id
    q = db.query.projects(project_id)
    parsed = parse_project_query(q)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed


@app.post("/user")
def insert_user(user: User, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if not db.exists.user(token.github_id):
        gh = GitHub(token.github_at)

        # set defaults needed to create a useer
        user.id = gh.user.id
        user.login = gh.user.login
        user.name = gh.user.name
        user.pods = gh.get_pods()
        
        db.insert.user(user)
    return status.HTTP_200_OK


@app.put("/user")
def update_user(user: User, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if db.exists.user(token.github_id):
        gh = GitHub(token.github_at)

        # set defaults needed to create a useer
        user.id = gh.user.id
        user.login = gh.user.login
        user.name = gh.user.name
        
        db.insert.update(user)
        return status.HTTP_200_OK
    else:
        return status.HTTP_400_BAD_REQUEST


@app.get("/user/{login}")
def query_user(login):
    query = db.query.users(login)
    parsed = parse_user_query(query)
    if parsed is None:
        return status.HTTP_404_NOT_FOUND
    else:
        return parsed

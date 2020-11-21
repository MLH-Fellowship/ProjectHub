from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from starlette import status
from slugify import slugify
from app.models import MicroUser, ExplorePage
from app.utils import jwe
from app.utils.github import GitHub
import app.utils.database as db
from app.apiparse import parse_project_query
from app.models import Project, User
from app.utils.jwe import HTTPBearerJWEScheme, HTTPAuthorizationJWT

app = FastAPI()
http_bearer_scheme = HTTPBearerJWEScheme(auth_optional=['/projects'])


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
def new_project(project: Project, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    project.owner = token.github_id
    project.slug = slugify(project.name)
    db.insert.project(project)
    # TODO: set project.id / not needed for ui
    return project


@app.put("/project")
def update_project(json: Project, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if db.exists.project(json):
        db.update.project(json)
    else:
        raise HTTPException(status.HTTP_404_BAD_REQUEST, 'Project not found')

@app.get("/projects")
def get_projects(token: Optional[HTTPAuthorizationJWT] = Depends(http_bearer_scheme)):
    projects = db.query.projects()
    
    pods = set()
    languages = set()

    for project in projects:
        user = db.query.user(id=project.owner)
        
        project.user = MicroUser(
            login=user.login,
            name=user.name,
            bio=user.bio,
            pods=user.pods,
            avatar=user.avatar,
            github=user.github,
        )

        if token:
           project.bookmarked = db.exists.bookmark(token.github_id, project.id)

        for pod in user.pods:
            pods.add(pod)

        for language in project.languages:
            languages.add(language)

    return ExplorePage(projects=projects, pods=list(pods), languages=list(languages))


@app.post("/user")
def insert_user(user: User, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if not db.exists.user(token.github_id):
        gh = GitHub(token.github_at)

        # set defaults needed to create a useer
        user.id = gh.user.id
        user.login = gh.user.login
        user.name = gh.user.name
        user.avatar = gh.user.avatar_url
        user.github = gh.user.html_url
        
        db.insert.user(user)


@app.post("/bookmark/{project_id}")
def upsert_bookmark(project_id: int, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if db.exists.bookmark(token.github_id, project_id):
        db.delete.bookmark(token.github_id, project_id)
    else:
        db.insert.bookmark(token.github_id, project_id)


@app.put("/user")
def update_user(user: User, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    if db.exists.user(token.github_id):
        gh = GitHub(token.github_at)

        # set defaults needed to create a useer
        user.id = gh.user.id
        user.login = gh.user.login
        user.name = gh.user.name
        user.avatar = gh.user.avatar_url
        user.github = gh.user.html_url
        
        db.insert.update(user)
        return
    raise HTTPException(status.HTTP_400_BAD_REQUEST, 'User not found')


@app.get("/user/bookmarks")
def query_user_bookmarks(token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    projects = db.query.projects_by_user_bookmarks(token.github_id)

    pods = set()
    languages = set()

    for project in projects:
        for language in project.languages:
            languages.add(language)

        user = db.query.user(id=project.owner)
        project.user = MicroUser(
            login=user.login,
            name=user.name,
            bio=user.bio,
            pods=user.pods,
            avatar=user.avatar,
            github=user.github,
        )

        for pod in user.pods:
            pods.add(pod)

        project.bookmarked = db.exists.bookmark(token.github_id, project.id)

    return ExplorePage(projects=projects, languages=list(languages), pods=list(pods))

@app.get("/user/{login}")
def query_user(login, token: HTTPAuthorizationJWT = Depends(http_bearer_scheme)):
    user = db.query.user(login=login)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    else:
        projects = db.query.user_projects(user.id)

        languages = set()

        for project in projects:
            for language in project.languages:
                languages.add(language)
            
            project.bookmarked = db.exists.bookmark(token.github_id, project.id)
        
        user.explorer = ExplorePage(projects=projects, languages=list(languages))

        return user
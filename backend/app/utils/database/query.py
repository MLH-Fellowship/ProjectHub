from typing import List
from . import connection
from app.models import User, Project

def list_from_commas(s):
    if s:
        return s.split(',')
    return []

def user_projects(owner: int) -> List[Project]:
    conn = connection.create()
    cur = conn.cursor()

    cur.execute("SELECT id, owner, slug, name, description, source, demo, tags, languages, state FROM projects WHERE owner=%s", (owner,))

    projects = []

    for ret in cur.fetchall():
        (id, owner, slug, name, description, source, demo, tags, languages, state) = ret
        projects.append(Project(
            id=id,
            owner=owner,
            slug=slug,
            name=name,
            description=description,
            source=source,
            demo=demo,
            tags=list_from_commas(tags),
            languages=list_from_commas(languages),
            state=state,
        ))

    return projects


def projects() -> List[Project]:
    conn = connection.create()
    cur = conn.cursor()

    cur.execute("SELECT id, owner, slug, name, description, source, demo, tags, languages, state FROM projects")

    projects = []

    for ret in cur.fetchall():
        (id, owner, slug, name, description, source, demo, tags, languages, state) = ret
        projects.append(Project(
            id=id,
            owner=owner,
            slug=slug,
            name=name,
            description=description,
            source=source,
            demo=demo,
            tags=list_from_commas(tags),
            languages=list_from_commas(languages),
            state=state,
        ))

    return projects


def user(login=None, id=None) -> User:
    st = "SELECT id, login, avatar, github, name, timezone_offset, bio, skills, interests, pods FROM users WHERE "
    if login:
        st += "login=%s"
    elif id:
        st += "id=%s"
    else:
        raise ValueError('must set login or id')

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (login or id,))
    res = cur.fetchone()

    if not res:
        return None

    (id, login, avatar, github, name, timezone_offset, bio, skills, interests, pods) = res

    return User(
        id=id,
        login=login,
        avatar=avatar,
        github=github,
        name=name,
        timezone_offset=timezone_offset,
        bio=bio,
        skills=list_from_commas(skills),
        interests=list_from_commas(interests),
        pods=list_from_commas(pods)
    )

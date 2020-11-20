from typing import List
from . import connection
from app.models import User, Project

def user_projects(owner: int) -> List[Project]:
    conn = connection.create()
    cur = conn.cursor()

    cur.execute("SELECT id, owner, slug, name, description, source, demo, tags FROM projects WHERE owner=%s", (owner,))

    projects = []

    for ret in cur.fetchall():
        (id, owner, slug, name, description, source, demo, tags) = ret
        projects.append(Project(
            id=id,
            owner=owner,
            slug=slug,
            name=name,
            description=description,
            source=source,
            demo=demo,
            tags=tags.split(','))
        )

    return projects


def users(login) -> User:
    st = "SELECT id, login, name, timezone_offset, bio, skills, interests, pods FROM users WHERE login=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (login,))
    res = cur.fetchone()

    if not res:
        return None

    (id, login, name, timezone_offset, bio, skills, interests, pods) = res

    return User(
        id=id,
        login=login,
        name=name,
        timezone_offset=timezone_offset,
        bio=bio,
        skills=skills.split(','),
        interests=interests.split(','),
        pods=pods.split(',')
    )

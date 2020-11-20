from . import connection
from app.models import User

def projects(project):
    st = "SELECT * FROM projects WHERE name=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (project,))

    return cur.fetchone()


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

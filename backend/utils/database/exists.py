from . import connection


def project(json):
    id = json.id
    st = "SELECT id FROM projects WHERE id=%s"
    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (id, ))
    return cur.fetchone() is not None


def user(json):
    username = json.username

    st = "SELECT id FROM users WHERE id=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (username,))

    return cur.fetchone() is not None

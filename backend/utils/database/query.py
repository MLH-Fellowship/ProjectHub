from . import connection


def projects(project):
    st = "SELECT id FROM projects WHERE name=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (project,))

    return cur.fetchone()


def users(username):
    st = "SELECT * FROM users WHERE username=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (username,))

    return cur.fetchone()

from . import connection


def projects(project):
    st = "SELECT * FROM projects WHERE name=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (project,))

    return cur.fetchone()


def users(id):
    st = "SELECT * FROM users WHERE id=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (id,))

    return cur.fetchone()

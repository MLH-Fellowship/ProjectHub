from . import connection


def project(rid):
    conn = connection.create()
    cur = conn.cursor()
    cur.execute("SELECT id FROM projects WHERE id=%d", (rid, ))
    return cur.fetchone() is not None


def user(rid):
    conn = connection.create()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE id=%d", (rid,))
    return cur.fetchone() is not None

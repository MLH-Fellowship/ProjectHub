from . import connection


def project(rid):
    conn = connection.create()
    cur = conn.cursor()
    cur.execute("SELECT id FROM projects WHERE id=%s", (rid, ))
    return cur.fetchone() is not None


def user(rid):
    conn = connection.create()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE id=%s", (rid,))
    return cur.fetchone() is not None


def bookmark(user_id, project_id):
    conn = connection.create()
    cur = conn.cursor()
    cur.execute("SELECT id FROM bookmarks WHERE user_id=%s AND project_id=%s", (user_id, project_id))
    return cur.fetchone() is not None

from . import connection

def project(json):
    id = json.id
    st = "SELECT id FROM projects WHERE id=%s" % (id,)
    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st)
    return cur.fetchone() is not None

def user(json):
    username = json.username

    st = "SELECT username FROM users WHERE username=%s" % (username,)

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st)

    return cur.fetchone() is not None
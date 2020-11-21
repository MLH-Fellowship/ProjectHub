from . import connection
from app.models import User
from app.models import Project


def bookmark(user_id, project_id):
    conn = connection.create()

    # Accesses the server, executes a command, and commits it
    cur = conn.cursor()
    cur.execute("DELETE FROM bookmarks WHERE user_id=%s AND project_id=%s", (user_id, project_id))
    conn.commit()

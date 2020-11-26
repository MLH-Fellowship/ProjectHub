from app.models import Project, UserUpdateModel
from . import connection


def project(project: Project): 
    conn = connection.create()
    cur = conn.cursor()

    cur.execute(
        "UPDATE projects SET name=%s, description=%s, source=%s, demo=%s, tags=%s, languages=%s, state=%s WHERE id=%s",
        (project.name, project.description, project.source, project.demo, ','.join(project.tags), ','.join(project.languages), project.state, project.id ))
    conn.commit()


def user(uid: int, user: UserUpdateModel):
    conn = connection.create()
    cur = conn.cursor()

    cur.execute(
        "UPDATE users SET bio=%s, pods=%s, skills=%s, interests=%s WHERE id=%s",
        (user.bio, ','.join(user.pods), ','.join(user.skills), ','.join(user.interests), uid)
    )
    conn.commit()

from app.models import Project
from . import connection


def project(project: Project): 
    conn = connection.create()
    cur = conn.cursor()

    cur.execute(
        "UPDATE projects SET name=%s, description=%s, source=%s, demo=%s, tags=%s, languages=%s, state=%s WHERE id=%s",
        (project.name, project.description, project.source, project.demo, ','.join(project.tags), ','.join(project.languages), project.state, project.id ))
    conn.commit()


def user(json):
    id = json.id
    login = json.login
    name = json.name
    pods = json.pods
    timezone_offset = json.timezone_offset
    bio = json.bio
    skills = ','.join(json.skills)
    interests = ','.join(json.interests)

    st = "UPDATE users SET login=%s, name=%s, pods=%s, timezone_offset=%s, bio=%s, skills=%s, interests=%s WHERE id=%s"

    conn = connection.create()
    cur = conn.cursor()

    cur.execute(st, (login, name, pods, timezone_offset, bio, skills, interests, id,))
    conn.commit()

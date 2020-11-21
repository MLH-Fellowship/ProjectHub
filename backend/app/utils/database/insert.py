from . import connection
from app.models import User
from app.models import Project


def project(project: Project):
    tags = ",".join(project.tags)
    languages = ','.join(project.languages)

    columns = ["owner", "slug", "name", "description", "source", "demo", "tags", "languages", "state"]
    values = [project.owner, project.slug, project.name, project.description, project.source, project.demo, tags, languages, project.state]

    connection.insert(
        column_names=columns,
        values=values,
        table_name="projects"
    )


def user(user: User):
    skills = ','.join(user.skills)
    interests = ','.join(user.interests)
    pods = ','.join(user.pods)

    columns = ["id", "login", "github", "avatar", "name", "pods", "timezone_offset", "bio", "skills", "interests"]
    values = [user.id, user.login, user.github, user.avatar, user.name, pods, user.timezone_offset, user.bio, skills, interests]

    connection.insert(
        column_names=columns,
        values=values,
        table_name="users"
    )

from . import connection
from app.models import User
from app.models import Project

project_columns = ["id serial PRIMARY KEY", "name text", "description text", "link text", "demo_link text", "image_url text", "tags text"]
user_columns = ["username text PRIMARY KEY", "name text", "photo text", "timezone text"]
project_table = "projects"
user_table = "users"


def project(project: Project):
    tags = ",".join(project.tags)
    languages = ','.join(project.languages)

    columns = ["owner", "slug", "name", "description", "source", "demo", "tags", "languages"]
    values = [project.owner, project.slug, project.name, project.description, project.source, project.demo, tags, languages]

    connection.insert(
        column_names=columns,
        values=values,
        table_name=project_table
    )


def user(user: User):
    skills = ','.join(user.skills)
    interests = ','.join(user.interests)
    pods = ','.join(user.pods)

    columns = ["id", "login", "name", "pods", "timezone_offset", "bio", "skills", "interests"]
    values = [user.id, user.login, user.name, pods, user.timezone_offset, user.bio, skills, interests]

    connection.insert(
        column_names=columns,
        values=values,
        table_name=user_table
    )

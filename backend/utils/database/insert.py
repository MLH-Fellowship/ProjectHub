from . import connection
from models import User

project_columns = ["id serial PRIMARY KEY", "name text", "description text", "link text", "demo_link text", "image_url text", "tags text"]
user_columns = ["username text PRIMARY KEY", "name text", "photo text", "timezone text"]
project_table = "projects"
user_table = "users"


def project(json):
    name = json.name
    description = json.description
    link = json.source_link
    demo_link = json.demo_link
    image_url = json.images
    tags = ",".join(json.tags)

    columns = ["name", "description", "link", "demo_link", "image_url", "tags"]
    values = [name, description, link, demo_link, image_url, tags]

    connection.execute_statement(column_names=columns,
                                 values=values,
                                 table_name=project_table
                                 )


def user(json: User):

    id = json.id
    username = json.username
    fullname = json.fullname
    pods = json.pods
    timezone = json.timezone
    bio = json.bio
    skills = json.skills
    interests = json.interests

    columns = ["id", "username", "fullname", "pods", "timezone", "bio", "skills", "interests"]
    values = [id, username, fullname, pods, timezone, bio, skills, interests]

    connection.execute_statement(column_names=columns,
                                 values=values,
                                 table_name=user_table
                                 )

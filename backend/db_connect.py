import psycopg2
from settings import *


class Connection(object):

    # environment variables pulled from .env file
    def __init__(self):
        self.host = POSTGRES_HOST
        self.database = POSTGRES_DATABASE
        self.port = POSTGRES_PORT
        self.username = POSTGRES_USER
        self.password = POSTGRES_PASSWORD

    # Creates a connection with the PostgreSQL server
    def create_connection(self):
        """
        :return: server connection
        """

        conn = None

        try:
            conn = psycopg2.connect(dbname=self.database,
                                    host=self.host,
                                    user=self.username,
                                    password=self.password,
                                    port=self.port)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return conn

    # Generates a table creation statement
    @staticmethod
    def generate_table_creation(table_name: str, column_names: list):
        """
        :param table_name:
        :param column_names:
        :return: SQL statement
        """

        items = ", ".join(column_names)
        items = "({})".format(items)
        statement = "CREATE TABLE IF NOT EXISTS %s%s" % (table_name, items,)

        return statement

    # Generates a insert into table statement. Includes some error checking
    @staticmethod
    def generate_insert_statement(table_name: str, column_names: list, values: list):
        """
        :param table_name: str
        :param column_names: list
        :param values: list
        :return: SQL statement
        """

        if len(column_names) == 0:
            raise IndexError("You can't insert an empty statement!")
        if len(column_names) != len(values):
            raise ValueError("Number of columns and number of values does not match.")

        items = ", ".join(values)
        items = "({})".format(items)

        columns = ", ".join(column_names)
        columns = "({})".format(columns)

        statement = "INSERT INTO %s%s VALUES %s" % (table_name, columns, items,)

        return statement

    # Executes a statement,
    def execute_statement(self, table_name: str, column_names: list, values=None):
        """
        :param table_name: str
        :param column_names: list
        :param values: optional list
        :return: Null
        """

        if len(column_names) == 0:
            raise ValueError("Must include column names")

        if values is not None and len(column_names) != len(values):
            raise ValueError("Number of columns and number of values must match")

        conn = self.create_connection()

        if values is None:
            raise ValueError("Values must be provided to be inserted into database")

        st = self.generate_insert_statement(table_name, column_names, values)

        # Accesses the server, executes a command, and commits it
        cur = conn.cursor()
        cur.execute(st)
        conn.commit()

        return


class Insert(object):

    def __init__(self):
        self.connection = Connection()
        self.project_columns = ["id serial PRIMARY KEY", "name text", "description text", "link text", "demo_link text", "image_url text", "tags text"]
        self.user_columns = ["username text PRIMARY KEY", "name text", "photo text", "timezone text"]
        self.project_table = "projects"
        self.user_table = "users"

    def insert_project(self, json):
        name = json.name
        description = json.description
        link = json.source_link
        demo_link = json.demo_link
        image_url = json.images
        tags = ",".join(json.tags)
        authors = ",".join(json.authors)

        columns = ["name", "description", "link", "demo_link", "image_url", "tags", "authors"]
        values = [name, description, link, demo_link, image_url, tags, authors]

        self.connection.execute_statement(column_names=columns,
                                          values=values,
                                          table_name=self.project_table
                                          )

        return

    def insert_user(self, json):
        username = json.username
        fullname = json.fullname
        pods = json.pods
        timezone = json.timezone
        bio = json.bio
        skills = json.skills
        interests = json.interests

        columns = ["username", "fullname", "pods", "timezone", "bio", "skills", "interests"]
        values = [username, fullname, pods, timezone, bio, skills, interests]

        self.connection.execute_statement(column_names=columns,
                                          values=values,
                                          table_name=self.user_table
                                          )

        return


class Update(object):

    def __init__(self, json):
        self.connection = Connection()
        self.json = json

    def project_exists(self):
        id = self.json.id
        st = "SELECT id FROM projects WHERE id=%s" % (id,)
        conn = self.connection.create_connection()
        cur = conn.cursor()

        cur.execute(st)
        return cur.fetchone() is not None

    def update_project(self):
        name = self.json.name
        description = self.json.description
        source_link = self.json.source_link
        demo_link = self.json.demo_link
        tags = ','.join(self.json.tags)
        authors = ','.join(self.json.authors)
        id = self.json.id

        st = "UPDATE projects SET name=%s, description=%s, source_link=%s, demo_link=%s, images=%s, tags=%s, authors=%s WHERE id=%s" % (name, description, source_link, demo_link, images, tags, authors, id,)

        conn = self.connection.create_connection()
        cur = conn.cursor()

        cur.execute(st)
        conn.commit()

        return

    def user_exists(self):
        username = self.json.username

        st = "SELECT username FROM users WHERE username=%s" % (username,)

        conn = self.connection.create_connection()
        cur = conn.cursor()

        cur.execute(st)

        return cur.fetchone() is not None

    def update_user(self):
        username = self.json.username
        fullname = self.json.name
        timezone = self.json.timezone
        bio = self.json.bio
        skills = ','.join(self.json.skills)
        interests = ','.join(self.json.interests)

        st = "UPDATE users SET fullname=%s, timezone=%s, bio=%s, skills=%s, interests=%s WHERE username=%s" % (fullname, timezone, bio, skills, interests, username, )

        conn = self.connection.create_connection()
        cur = conn.cursor()

        cur.execute(st)
        conn.commit()

        return


class Query(object):

    def __init__(self):
        self.conn = Connection().create_connection()

    def query_projects(self, project):
        st = "SELECT id FROM projects WHERE name=%s" % (project,)

        cur = self.conn.cursor()

        cur.execute(st)

        return cur.fetchone()

    def query_users(self, username):
        st = "SELECT * FROM users WHERE username=%s" % (username,)

        cur = self.conn.cursor()

        cur.execute(st)

        return cur.fetchone()

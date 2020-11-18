import psycopg2
import os
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
        statement = "CREATE TABLE IF NOT EXISTS {}{}".format(table_name, items)

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

        statement = "INSERT INTO {}{} VALUES {}".format(table_name, columns, items)

        return statement

    # Executes a statement,
    def execute_statement(self, statement: str, table_name: str, column_names: list, values=None):
        """
        :param statement: str
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

        if statement == "table":
            st = self.generate_table_creation(table_name, column_names)

        elif statement == "insert":
            if values is None:
                raise ValueError("Values must be provided to be inserted into database")

            st = self.generate_insert_statement(table_name, column_names, values)

        else:
            raise ValueError("Invalid statement type, must be \"table\" or \"insert\"")

        # Accesses the server, executes a command, and commits it
        cur = conn.cursor()
        cur.execute(st)
        conn.commit()

        return

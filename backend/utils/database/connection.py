import psycopg2
from settings import POSTGRES_HOST, POSTGRES_DATABASE, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD


# Creates a connection with the PostgreSQL server
def create():
    """
    :return: server connection
    """

    conn = None

    try:
        conn = psycopg2.connect(dbname=POSTGRES_DATABASE,
                                host=POSTGRES_HOST,
                                user=POSTGRES_USER,
                                password=POSTGRES_PASSWORD,
                                port=POSTGRES_PORT)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn


# Generates a insert into table statement. Includes some error checking
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


# Executes a statement,
def execute_statement(table_name: str, column_names: list, values: list):
    """
    :param table_name: str
    :param column_names: list
    :param values: optional list
    :return: Null
    """

    if len(column_names) == 0:
        raise ValueError("Must include column names")

    statement = f"INSERT INTO {table_name}({', '.join(column_names)}) VALUES({', '.join('%s' for _ in range(len(values)))})"
    print(statement)

    conn = create()

    # Accesses the server, executes a command, and commits it
    cur = conn.cursor()
    cur.execute(statement, values)
    conn.commit()

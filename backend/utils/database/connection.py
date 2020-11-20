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

# Generates a table creation statement
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
def execute_statement(table_name: str, column_names: list, values=None):
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

    conn = create()

    if values is None:
        raise ValueError("Values must be provided to be inserted into database")

    st = generate_insert_statement(table_name, column_names, values)

    # Accesses the server, executes a command, and commits it
    cur = conn.cursor()
    cur.execute(st)
    conn.commit()

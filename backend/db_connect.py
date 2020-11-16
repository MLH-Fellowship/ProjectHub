import psycopg2
import sys

class Connection(object):

    def __init__(self, fromLocal=True):
        if fromLocal:
            self.host = ""
            self.database = ""
            self.username = ""
            self.password = ""
        else:
            self.host = sys.argv[1]
            self.database = sys.argv[2]
            self.username = sys.argv[3]
            self.password = sys.argv[4]

    def create_connection(self):
        conn = None

        try:
            conn = psycopg2.connect(dbname=self.database,
                                    host=self.host,
                                    user=self.username,
                                    password=self.password,
                                    port=25060)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        return conn

    @staticmethod
    def generate_table_creation(table_name, column_names):
        items = ", ".join(column_names)
        items = "({})".format(items)
        statement = "CREATE TABLE IF NOT EXISTS {}{}".format(table_name, items)

        return statement

    @staticmethod
    def generate_insert_statement(table_name, column_names, values):
        items = ", ".join(values)
        items = "({})".format(items)

        columns = ", ".join(column_names)
        columns = "({})".format(columns)

        statement = "INSERT INTO {}{} VALUES {}".format(table_name, columns, items)

        return statement

    def execute_statement(self, statement, table_name, column_names, values=None):
        conn = self.create_connection()

        if statement == "table":
            st = self.generate_table_creation(table_name, column_names)

        elif statement == "insert":
            if values is None:
                raise ValueError("You must have values")
            elif len(values) != len(column_names):
                raise ValueError("Number of value must equal number of columns")
            else:
                st = self.generate_insert_statement(table_name, column_names, values)
        else:
            raise ValueError("Statement type must be valid")

        cur = conn.cursor()
        cur.execute(st)
        conn.commit()

        return



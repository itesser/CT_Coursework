from dotenv import load_dotenv
from os import getenv
import psycopg2

load_dotenv()

user = getenv("USER")
password = getenv("PASSWORD")
server = getenv("SERVER")

pg_connection = psycopg2.connect(dbname=user, user=user, password=password, host=server)

cur = pg_connection.cursor()


def read_sql_file(fpath: str):
    """open a sql file and read it and return it in the function"""
    with open(fpath, "r") as f:
        sql_file = f.read()
    return sql_file


def create_tables(sql_filepath: str):
    start = read_sql_file(sql_filepath)
    tables = start.split(";")
    for table in tables:
        try:
            print(table)
            cur.execute(table)
            pg_connection.commit()
        except psycopg2.ProgrammingError as msg:
            print(f"Command skipped {msg}")


def insert_data(sql_filepath: str):
    start = read_sql_file(sql_filepath)
    commands = start.split(";")
    for command in commands:
        try:
            print(command)
            cur.execute(command)
            pg_connection.commit()
        except psycopg2.ProgrammingError as msg:
            print(f"Command skipped {msg}")


if __name__ == "__main__":
    create_tables("ecomm_mock_create.sql")
#    insert_data('ecomm_mock_insert.sql')

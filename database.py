import sqlite3


CREATE_BATCH_TABLE = """
    CREATE TABLE batch
               (id integer,
                type text,
                t text,
                symbol text,
                qty real,
                price real)
"""

CREATE_LOG_TABLE = """"""


def connect(file):
    return sqlite3.connect(file)

def create_tables(connection):
    with connection:
        connection.execute(CREATE_BATCH_TABLE)
        connection.execute(CREATE_LOG_TABLE)


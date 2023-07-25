```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"C:\sqlite\db\ai_prank_dialer.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        preferences text
                                    ); """

    sql_create_calls_table = """CREATE TABLE IF NOT EXISTS calls (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    scheduled_time text NOT NULL,
                                    script text NOT NULL,
                                    recording text,
                                    FOREIGN KEY (user_id) REFERENCES users (id)
                                );"""

    sql_create_recordings_table = """CREATE TABLE IF NOT EXISTS recordings (
                                        id integer PRIMARY KEY,
                                        call_id integer NOT NULL,
                                        recording_path text NOT NULL,
                                        FOREIGN KEY (call_id) REFERENCES calls (id)
                                    );"""

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_calls_table)
        create_table(conn, sql_create_recordings_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```
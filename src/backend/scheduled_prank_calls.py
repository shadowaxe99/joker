```python
import sqlite3
from sqlite3 import Error

# Database connection
def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')       
        print(f'successful SQLite connection with id {id(conn)}')
    except Error as e:
        print(e)
    
    if conn:
        return conn

# Create scheduled_calls table
def create_scheduled_calls_table(conn):
    try:
        sql = '''CREATE TABLE scheduled_calls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    prank_call_id INTEGER NOT NULL,
                    scheduled_time TEXT NOT NULL,
                    status TEXT NOT NULL
                );'''
        conn.execute(sql)
    except Error as e:
        print(e)

# Insert scheduled call
def insert_scheduled_call(conn, scheduled_call):
    sql = '''INSERT INTO scheduled_calls(user_id, prank_call_id, scheduled_time, status)
             VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, scheduled_call)
    return cur.lastrowid

# Get all scheduled calls
def get_all_scheduled_calls(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM scheduled_calls")
    rows = cur.fetchall()
    return rows

# Update scheduled call status
def update_scheduled_call_status(conn, id, status):
    sql = ''' UPDATE scheduled_calls
              SET status = ? 
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (status, id))
    conn.commit()

# Delete a scheduled call
def delete_scheduled_call(conn, id):
    sql = 'DELETE FROM scheduled_calls WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# Store scheduled call
def store_scheduled_call(user_id, prank_call_id, scheduled_time):
    conn = create_connection()
    create_scheduled_calls_table(conn)
    scheduled_call = (user_id, prank_call_id, scheduled_time, "Scheduled")
    insert_scheduled_call(conn, scheduled_call)
    print("Scheduled call stored successfully.")
    conn.close()
```
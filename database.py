import sqlite3

def get_connection():
    conn = sqlite3.connect("tasks.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tasks(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   priority TEXT,
                   status BOLLEAN DEFAULT 0,
                   due_date TEXT
                   )
                   """)
    
    conn.commit()
    conn.close()

def insert_task(name,priority,due_date):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks(name,priority,due_date)
    VALUES(?,?,?)
    """,(name,priority,due_date))

    conn.commit()
    conn.close()
    
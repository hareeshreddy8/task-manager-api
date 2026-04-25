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

def get_all_tasks():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()

    conn.close()
    tasks = []
    #converting tuple data into json format for api
    for row in rows:
        task = {
            "id": row[0],
            "name": row[1],
            "priority": row[2],
            "status": bool(row[3]),
            "due_date": row[4]
        }

        tasks.append(task)
    return tasks
def update_task_status(task_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET status = 1
    WHERE id = ?
    """,(task_id,))
    conn.commit()

    cursor.execute("SELECT * FROM tasks WHERE id = ?",(task_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "name": row[1],
            "priority": row[2],
            "status": bool(row[3]),
            "due_date": row[4]
        }
    return None

def delete_data(task_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM tasks WHERE id = ?""",(task_id,))
    row = cursor.fetchone()
    if not row :
        conn.close()
        return None
    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
        """,(task_id,))
    
    conn.commit()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "priority": row[2],
            "status": bool(row[3]),
            "due_date": row[4]
        }
    return None

def edit_data_name(task_id,name):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
                UPDATE tasks
                SET name = ?
                WHERE id = ?
                """,(name,task_id))
    
    conn.commit()

    cursor.execute("""SELECT * FROM tasks WHERE id = ?""",(task_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "priority": row[2],
            "status": bool(row[3]),
            "due_date": row[4]
        }
    return None

def filter_data(priority = None,status = None):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if priority:
        query += " AND priority = ?"
        params.append(priority)

    if status is not None :
        query += " AND status = ?"
        params.append(status)

    cursor.execute(query,params)

    rows = cursor.fetchall()
    conn.close()

    return rows
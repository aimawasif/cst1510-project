# db_helper.py
import sqlite3
from pathlib import Path

BASE = Path.cwd()
DB_DIR = BASE / "data"
DB_DIR.mkdir(exist_ok=True)
DB_PATH = DB_DIR / "myTest.db"

def get_conn(path=DB_PATH):
    """Return a sqlite3 connection with row factory and foreign keys ON."""
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
import sqlite3

DB_NAME = "myTest.db"

# --------------------------------------
# CONNECT TO DATABASE
# --------------------------------------
def get_conn():
    return sqlite3.connect(DB_NAME)

# --------------------------------------
# CREATE TABLE
# --------------------------------------
def create_table():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                role TEXT DEFAULT 'user'
            )
        """)
        conn.commit()

# --------------------------------------
# INSERT RECORD
# --------------------------------------
def insert_user(username, email, role="user"):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users_data (username, email, role)
            VALUES (?, ?, ?)
        """, (username, email, role))
        conn.commit()

# --------------------------------------
# FETCH ALL USERS
# --------------------------------------
def get_all_users():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users_data")
        return cursor.fetchall()

# --------------------------------------
# UPDATE USER
# --------------------------------------
def update_user(user_id, new_email):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users_data
            SET email = ?
            WHERE id = ?
        """, (new_email, user_id))
        conn.commit()

# --------------------------------------
# DELETE USER
# --------------------------------------
def delete_user(user_id):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users_data WHERE id = ?", (user_id,))
        conn.commit()

import sqlite3

with sqlite3.connect('myTest.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())
import sqlite3

with sqlite3.connect('myTest.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()
    print("Users table content:", rows)

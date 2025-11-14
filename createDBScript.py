import sqlite3

# Create or connect to the database
with sqlite3.connect('myTest.db') as conn:
    cursor = conn.cursor()
    print("Connected to database!")

    createTableScript = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        role TEXT DEFAULT 'user'
    )"""

    # Create table inside the connection block
    cursor.execute(createTableScript)
    conn.commit()
    print("Table created successfully!")

print("Process finished with exit code 0")

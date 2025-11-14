import sqlite3

with sqlite3.connect('myTest.db') as conn:
    cursor = conn.cursor()
    print("Connected to database!")

    # Create table
    create_table_script = """
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        role TEXT DEFAULT 'user'
    )
    """
    cursor.execute(create_table_script)

    # Example username to insert
    username_to_insert = 'abc2'
    role_to_insert = 'user'

    # Check if username exists before inserting
    cursor.execute("SELECT * FROM users WHERE username=?", (username_to_insert,))
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO users (username, role) VALUES (?, ?)",
            (username_to_insert, role_to_insert)
        )
        print(f"Inserted '{username_to_insert}' successfully!")
    else:
        print(f"Username '{username_to_insert}' already exists. Skipping insert.")

    # Fetch and display all users
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Users Table Content:")
    for user in users:
        print(user)

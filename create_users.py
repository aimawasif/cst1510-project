import sqlite3
import bcrypt
import csv
from db import get_connection

CSV_FILE = "weak_credentials.csv"  # path to your CSV

# ---------------- Password Hashing ----------------
def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

# ---------------- Create Users Table ----------------
def create_users_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    print("Users table ensured.")

# ---------------- Add Admin User ----------------
def add_admin_user():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", ("admin",))
    if cur.fetchone():
        print("Admin user already exists.")
    else:
        cur.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin", hash_password("admin123"), "admin")
        )
        conn.commit()
        print("Admin user created: username='admin', password='admin123'")
    conn.close()

# ---------------- Load Users from CSV ----------------
def load_users_from_csv(csv_file):
    conn = get_connection()
    cur = conn.cursor()
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row["username"]
            role = row.get("role", "user")
            # Use default password for all CSV users (can be improved later)
            password = row.get("default_password", "password123")
            hashed = hash_password(password)
            try:
                cur.execute(
                    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                    (username, hashed, role)
                )
                print(f"Added user: {username}")
            except sqlite3.IntegrityError:
                print(f"User {username} already exists, skipping.")
    conn.commit()
    conn.close()

# ---------------- Main ----------------
if __name__ == "__main__":
    create_users_table()
    add_admin_user()
    load_users_from_csv(CSV_FILE)
    print("Setup complete. You can now log in.")


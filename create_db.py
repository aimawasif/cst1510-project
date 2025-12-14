# create_db.py
from db import DatabaseManager

db = DatabaseManager()
db.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    role TEXT,
    password_hash BLOB
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS cyber_incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    incident_time TEXT,
    category TEXT,
    severity INTEGER,
    status TEXT,
    assigned_to TEXT,
    description TEXT
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS datasets_metadata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    owner TEXT,
    rows INTEGER,
    size_mb REAL,
    source TEXT,
    last_updated TEXT
);
""")

db.execute("""
CREATE TABLE IF NOT EXISTS it_tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TEXT,
    resolved_at TEXT,
    status TEXT,
    priority TEXT,
    assigned_to TEXT,
    wait_stage TEXT, -- e.g. 'Waiting for User'
    description TEXT
);
""")
print("schema created")

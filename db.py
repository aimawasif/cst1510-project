# db.py
import sqlite3
from pathlib import Path
import pandas as pd
from typing import Any, Dict, List, Tuple

DB_FILE = Path("myTest.db")  # your DB

class DatabaseManager:
    def __init__(self, db_path: Path = DB_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(str(db_path), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def execute(self, query: str, params: Tuple = ()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()
        return cur

    def fetchall(self, query: str, params: Tuple = ()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        return [dict(r) for r in cur.fetchall()]

    def fetchone(self, query: str, params: Tuple = ()):
        cur = self.conn.cursor()
        cur.execute(query, params)
        row = cur.fetchone()
        return dict(row) if row else None

    def close(self):
        self.conn.close()


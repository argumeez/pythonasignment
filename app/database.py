import sqlite3
import os
from config import settings


class Database:
    def __init__(self):
        os.makedirs(os.path.dirname(settings.DATABASE_PATH), exist_ok=True)
        self._create_tables()

    def _connect(self):
        return sqlite3.connect(settings.DATABASE_PATH)

    def _create_tables(self):
        conn = self._connect()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS practice_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                duration INTEGER NOT NULL,
                warmup INTEGER,
                exercises TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                target TEXT NOT NULL,
                completed INTEGER NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def execute_query(self, query, params=()):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def fetch_all(self, query, params=()):
        conn = self._connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return rows

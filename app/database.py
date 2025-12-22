import sqlite3
import os
from config import settings


class Database:
    def __init__(self):
        os.makedirs(os.path.dirname(settings.DATABASE_PATH), exist_ok=True)
        self.connection = sqlite3.connect(settings.DATABASE_PATH)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS practice_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                duration INTEGER NOT NULL,
                warmup INTEGER,
                exercises TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                target TEXT NOT NULL,
                completed INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        self.connection.close()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        self.connection.close()
        return rows

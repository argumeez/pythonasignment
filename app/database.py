import sqlite3
from config import settings

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(settings.DATABASE_PATH)
        self.cursor = self.connection.cursor()
        
    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()
        
    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()
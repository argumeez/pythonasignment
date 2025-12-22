import sqlite3
from config import settings


class Database: 
    def __init__(self, db_path=settings.DATABASE_PATH):
        self.db_path = db_path
        self.connection = None
        self.create_tables()


    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def create_tables(self):
        dbconnection = self.connect()
        cursor = dbconnection.cursor()
        
    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS practice_sessions (
              id integer PRIMARY KEY AUTOINCREMENT,
              date TEXT NOT NULL,
              duration INTEGER NOT NULL,
              warmup INTEGER,
              exercises TEXT
            )
        ''')
        
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS goals (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             description TEXT NOT NULL,
             target TEXT NOT NULL,
             completed BOOLEAN NOT NULL
           )
      ''')
           
        dbconnection.commit()
        dbconnection.close()
        
if __name__ == "__main__":
    db = Database()
    print("Database + tables are created")
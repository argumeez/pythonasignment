import csv 
import pandas as pd
from app.database import Database
import os
from config import settings

def generate_csv_report():
    db = Database()
    sessions = db.fetch_all("SELECT * FROM practice_sessions")
    goals = db.fetch_all("SELECT * FROM goals")
    
    
    # This will check if a data folder exists
    data_dir = os.path.dirname(settings.DATABASE_PATH)
    os.makedirs(data_dir, exist_ok=True)
    
    sessions_path = os.path.join(data_dir, "practice_sessions_report.csv")
    goals_path = os.path.join(data_dir, "goals_report.csv")
    
    with open(sessions_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'duration','warmup', 'exercises'])
        writer.writerows(sessions)
        
    with open(goals_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'description', 'target', 'completed'])
        writer.writerows(goals)
        
        
    print("CSV reports generated.")
    

def generate_excel_report():
    db = Database()
    sessions = db.fetch_all("SELECT * FROM practice_sessions")
    goals = db.fetch_all("SELECT * FROM goals")
    
    sessions_df = pd.DataFrame(sessions, columns=["id", "date", "duration", "warmup", "exercises"])
    goals_df = pd.DataFrame(goals, columns=["id", "description", "target", "completed"])
    
    with pd.ExcelWriter('practice_reports.xlsx') as writer:
        sessions_df.to_excel(writer, sheet_name="Practice Sessions", index=False)
        goals_df.to_excel(writer, sheet_name="Goals", index=False)
        
        
    print("Excel report generated.")
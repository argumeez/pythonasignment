import csv 
import pandas as pd
from app.database import Database

def generate_csv_report():
    db = Database()
    sessions = db.fetch_all("SELECT * FROM practice_sessions")
    goals = db.fetch_all("SELECT * FROM goals")
    
    with open('practice_sessions_report.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'date', 'duration','warmup', 'exercises'])
        writer.writerows(sessions)
        
    with open('goals_report.csv', 'w', newline='') as f:
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
        sessions_df.to_excel(writer, sheet_name="Practice Sessions")
        goals_df.to_excel(writer, sheet_name="Goals")
        
        
    print("Excel report generated.")
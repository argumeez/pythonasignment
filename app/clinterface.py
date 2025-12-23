from app.database import Database
import argparse
from app.report import generate_csv_report, generate_excel_report
from datetime import datetime


def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")

def add_practice_sessions(date, duration, warmup, exercises):
    validate_date(date)
    db = Database()
    db.execute_query("INSERT INTO practice_sessions (date, duration, warmup, exercises) VALUES (?,?,?,?)",
                     (date, int(duration), int(warmup), exercises),
    )
    print(f"Practice Sessions on {date} added.")
    

def add_goal(description, target, completed):
    db = Database()
    db.execute_query("INSERT INTO goals (description, target, completed) VALUES (?,?,?)",
                     (description, target, completed),
    )
    print(f"Goal '{description}' added")
    
def remove_practice(session_id):
    db = Database()
    db.execute_query("DELETE FROM practice_sessions WHERE ID = ?",
                     (int(session_id),)
    )
    print(f"Practice session {session_id} removed.")
    
def remove_goal(goal_id):
    db = Database()
    db.execute_query("DELETE FROM goals WHERE ID = ?",
                     (int(goal_id),)
    )
    print(f"Goal {goal_id} removed.")
    
    
def list_practice_sessions():
    db = Database()
    sessions = db.fetch_all("SELECT * FROM practice_sessions")
    for session in sessions:
        print(session)
        
def list_goals():
    db = Database()
    goals = db.fetch_all("SELECT * FROM goals")
    for goal in goals:
        print(goal)




def main():
    parser = argparse.ArgumentParser(description="Trumpet Practice Tracker")
    parser.add_argument('--add-practice', nargs=4)
    parser.add_argument('--add-goal', nargs=3)
    parser.add_argument('--list-practice', action='store_true')
    parser.add_argument('--list-goals', action='store_true')
    parser.add_argument('--remove-practice', nargs=1)
    parser.add_argument('--remove-goal', nargs=1)
    parser.add_argument('--generate-report-csv', action='store_true')
    parser.add_argument('--generate-report-excel', action='store_true')
    
    args = parser.parse_args()
    
    if args.add_practice:
        add_practice_sessions(*args.add_practice)
    elif args.add_goal:
        add_goal(*args.add_goal)
    elif args.list_practice:
        list_practice_sessions()
    elif args.list_goals:
        list_goals()
    elif args.remove_practice:
        remove_practice(args.remove_practice[0])
    elif args.remove_goal:
        remove_goal(args.remove_goal[0])
    elif args.generate_report_csv:
        generate_csv_report()
    elif args.generate_report_excel:
        generate_excel_report()
    else:
        print("No valid command.")
        
        
        
if __name__=='__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
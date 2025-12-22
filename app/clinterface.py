from app.database import Database
import argparse
from app.report import generate_csv_report, generate_excel_report


def add_practice_sessions(date, duration, warmup, exercises):
    db = Database()
    db.execute_query("INSERT INTO practice_sessions (date, duration, warmup, exercises) VALUES (?,?,?,?)",
                     (date, duration, warmup, exercises))
    print(f"Practice Sessions on {date} added.")
    

def add_goal(description, target, completed):
    db = Database()
    db.execute_query("INSERT INTO goals (description, target, completed) VALUES (?,?,?)",
                     (description, target, completed))
    print(f"Goal '{description}' added")
    
    
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
    parser = argparse.ArgumentParser(desciption="Trumpet Practice Tracker")
    parser.add_argument('--add-practice', nargs=4, metavar=('date', 'duration', 'warmup', 'exercises'),
                        help="Add a new practice session")
    parser.add_argument('--add-goal', nargs=3, metavar=('description', 'target', 'completed'),
                        help="Add a goal")
    parser.add_argument('--list-practice', action='store_true', help="List all practice sessions")
    parser.add_argument('--list-goals', action='store_true', help="List all goals")
    parser.add_arguemtn('--generate-report-csv', action='store_true', help="Generate a CSV report")
    parser.add_argument('--generate-report-excel', action='store_true', help="Generate an Excel report")
    
    args = parser.parse_args()
    
    if args.add_practice:
        add_practice_sessions(*args.add_practice)
    elif args.add_goal:
        add_goal(*args.add_goal)
    elif args.list_practice:
        list_practice_sessions()
    elif args.list_goals:
        list_goals()
    elif args.generate_report_csv:
        generate_csv_report()
    elif args.generate_report_excel:
        generate_excel_report()
    else:
        print("No valid command.")
        
        
        
if __name__=='__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
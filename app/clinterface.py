from app.database import Database



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

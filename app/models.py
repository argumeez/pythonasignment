class PracticeSessions: 
    def __init__(self, id, date, duration, warmup, exercises):
        self.id = id
        self.date = date
        self.duration = duration
        self.warmpup = warmup
        self.exercises = exercises
        
    def __str__(self):
        return f"Date: {self.date}, Duration: {self.duration} minutes, Warmup: {self.warmup}: Exercises: {self.exercises}"


    
class Goal: 
    def __init(self, id, description, target, completed):
        self.id = id
        self.description = description
        self.target = target
        self.completed = completed
        
    def __str__(self):
        return f"Goal: {self.description}, Target: {self.target}, Completed: {self.completed}"

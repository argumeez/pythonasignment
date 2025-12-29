# pythonasignment
Python command-line application with an SQLite database for storing, searching, and modifying data.

Trumpet Practice tracker

- Practice Sessions: contains data such as: total duration, warm-up time and exercises you worked on. 
- Goals: what you want to achieve and in how many days. For example: practice long tones daily for 30 days. 
- Report: total hourse practiced, how long you warmed up or exercis.


# How to use the application

File structure:
- TrumpetPracticePlanner (root folder)
  - app:
    - clinterface.py
    - database.py
    - models.py
    - report.py
  - config:
    - settings.py (the example.settings file is on github place the settings inside settings.py inside the config folder.
  - data:
    - trumpet_practice.db (this folder contains all the data like the database file. If you generate excel reports it will be placed in this folder.


Use the application:
- if you use spyder:
  - make sure you are in the right folder (root folder TrumpetPracticeTracker
  - for adding a practice: !python app/clinterface.py --add-practice "2025-12-22" 60 15 "Long Tones"
  - for removing a practice: !python app/clinterface.py --remove-practice 5 (the id of the practice)
  - for adding a goal: !python app/clinterface.py --add-goal "Practice long tones daily" "30 days" False
  - for removing a goal: !python app/clinterface.py --remove-goal 1 (id of the goal)
  - listing the practices: !python app/clinterface.py --list-practice
  - listing the goals: !python app/clinterface.py --list-goals
  - generating excel report: !python app/clinterface.py --generate-report-excel
  - generating csv report: !python app/clinterface.py --generate-report-csv

 - if you use cmd:
   - make sure you are in the correct folder (root folder TrumpetPracticeTracker
   - for addign a practice: python -m app.clinterface --add-practice "2025-12-29" 30 10 "Jazz"
   - for removing a pratice: python -m app.clinterface --remove-practice 5 (the id of the practice)
   - for adding a goal: python -m app.clinterface --add-goal "Practice long tones daily" "30 days" False
   - for removing a goal: python -m app.clinterface --remove-goal 1 (id of the goal)
   - listing the pratices: python -m app.clinterface --list-practice
   - listing the goals: python -m app.clinterface --list-goals
   - generating excel reports: python -m app.clinterface --generate-report-excel
   - generating csv report: python -m app.clinterface --generate-report-csv

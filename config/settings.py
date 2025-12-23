import os
#this code finds the base directory of the project. Changes it to an absolute path, and moves 2 folders up. 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Starts at BASE_DIR and goes into te data folder where it points to trumpet_practice.db
DATABASE_PATH = os.path.join(BASE_DIR, "data", "trumpet_practice.db")
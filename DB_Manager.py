# check in other project to see if
import sqlite3
from sqlite3 import Error


class DBManager:
    def __init__(self):
        try:
            conn = sqlite3.connect("\DB\database.db") # this isn't working figure this out next time
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            conn.close()


db = DBManager()


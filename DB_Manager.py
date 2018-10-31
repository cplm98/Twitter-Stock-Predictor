# check in other project to see if
import sqlite3
from sqlite3 import Error


class DBManager:
    # initialize connection to data base and set object conn
    def __init__(self, db_name):
        try:
            conn = sqlite3.connect(db_name) # this isn't working figure this out next time
            print(sqlite3.version)
            self.conn = conn
        except Error as e:
            print(e)


db = DBManager('C:\Projects\Twitter Stock Predictor\Twitter-Stock-Predictor\DB\database.db')


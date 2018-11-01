# check in other project to see if
import sqlite3
from sqlite3 import Error


class DBManager:
    # initialize connection to data base and set object conn
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name) # this isn't working figure this out next time
            print(sqlite3.version)
            self.c = self.conn.cursor()
        except Error as e:
            print(e)

    def create_tables(self):
        self.c.execute("CREATE TABLE IF NOT EXISTS Tweets(tweet_body TEXT, retweets INTEGER, "
                  "favourites INTEGER, verified BOOLEAN, follower_count INTEGER, sentiment TEXT, confidence INTEGER)") #convert confidence into an int
        # c.execute("CREATE TABLE IF NOT EXISTS Stock_Data") don't know what data I'm gonna use yet
        self.conn.commit()

    def store_tweet(self, data_list):  # tweet_body, retweets, favourites, verified, follower_count, sentiment, confidence):
        for data in data_list:
            if not self.tweet_exists(data[0]):
                self.c.execute("INSERT INTO Tweets VALUES(?, ?, ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            else:
                print("duplicate")
        self.conn.commit()




    def tweet_exists(self, tweet_text):
        self.c.execute("SELECT tweet_body FROM Tweets WHERE (tweet_body=?)", (tweet_text,))
        entry = self.c.fetchone()
        if entry is None:
            return False
        else:
            return True


db = DBManager('C:\Projects\Twitter Stock Predictor\Twitter-Stock-Predictor\DB\database.db')
db.create_tables()
db.store_tweet([('this is the tweet', 75, 34, True, 47, 'whatever', 69)])


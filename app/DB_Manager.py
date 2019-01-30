# check in other project to see if
import sqlite3
from datetime import datetime, timedelta
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
        self.c.execute("CREATE TABLE IF NOT EXISTS Tweets(time_stamp STRING, tweet_id STRING, user_id STRING, username String, tweet_body TEXT, retweets INTEGER, "
                       "favourites INTEGER, verified BOOLEAN, follower_count INTEGER, sentiment_confidence INTEGER)")  # convert confidence into an int
        self.c.execute("CREATE TABLE IF NOT EXISTS Stock_Data(time_stamp STRING, open_price INTEGER, close_price INTEGER)") #don't know what data I'm gonna use yet
        self.conn.commit()

    def store_stock_data(self, data_list):
        for data in data_list:
            if not self.entry_exists(data[0]):
                self.c.execute("INSERT INTO Stock_Data VALUES(?, ?, ?)", (data[0], data[1], data[2]))
            else:
                print("stock duplicate")
        self.conn.commit()  # really gotta stop forgetting to commit things

    def store_tweet(self, data_list):  # tweet_body, retweets, favourites, verified, follower_count, sentiment_confidence):
        for data in data_list:
            if not self.tweet_exists(data[1]):
                self.c.execute("INSERT INTO Tweets VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
            else:
                print("duplicate")
        self.conn.commit()

    def tweet_exists(self, tweet_id):
        self.c.execute("SELECT tweet_body FROM Tweets WHERE (tweet_id=?)", (tweet_id,))
        entry = self.c.fetchone()
        if entry is None:
            return False
        else:
            return True

    def entry_exists(self, time_stamp):
        self.c.execute("SELECT time_stamp FROM Stock_Data WHERE (time_stamp=?)", (time_stamp,))
        entry = self.c.fetchone()
        if entry is None:
            return False
        else:
            return True

    def get_ten_tweets(self):
        self.c.execute("SELECT * FROM Tweets")
        data = self.c.fetchmany(10)
        return data

    def scatter_format(self, dates, prices):
        newlist = []
        i = 0
        for h, w in zip(dates, prices):
            newlist.append({'x': i, 'y': w})
            i = i + 1 # could not get the times to work for the life of me so work on that later
        ugly_blob = str(newlist).replace('\'', '')
        return ugly_blob

    def scatter_formate2(self, dates, prices): # this gets the data to look completely right idk what the problem is now
        newlist = []
        for h, w in zip(dates, prices):
            newlist.append({'t': 'moment().toDate(' + h + ')', 'y': w})
            #newlist.append({'x': h, 'y': w})
        print(newlist)
        ugly_blob = str(newlist).replace('\'', '')
        print(ugly_blob)
        return ugly_blob

    def get_todays_data(self):
        prices = []
        dates = []
        self.c.execute("SELECT * FROM Stock_Data ORDER BY date(time_stamp) DESC")
        data = self.c.fetchmany(28)
        print("todays date: ", datetime.today().date())
        for obj in data:
            date = datetime.strptime(obj[0], '%Y-%m-%d %H:%M:%S')
            print(date)
            if date.date() == datetime.today().date() - timedelta(days=1):
                dates.append(str(date.time()))
                prices.append(obj[1]/100)
        print(dates)
        return self.scatter_format(dates, prices)

    def test_stock_data(self):
        self.c.execute("SELECT time_stamp close_price FROM Stock_Data")
        data = self.c.fetchmany(28)
        return data






# db = DBManager(r'C:\Projects\Twitter Stock Predictor\Twitter-Stock-Predictor\app\DB\database.db')
# db.create_tables()
# data = db.get_todays_data()
# print(data)

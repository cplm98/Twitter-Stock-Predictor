from flask import render_template
from app import app
from app.DB_Manager import DBManager
from datetime import datetime



@app.route('/')
def default():
    db = DBManager(r'C:\Projects\Twitter Stock Predictor\Twitter-Stock-Predictor\app\DB\database.db')
    db.create_tables()
    tweets = db.get_ten_tweets()
    data = db.get_todays_data()
    dates = [1, 2, 3, 4, 5]
    prices = [100, 124, 99, 87, 200]
    #print(tweets)
    return render_template("base.html", tweets=tweets, data=data)

@app.route('/test')
def test():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template("test.html", values=values, labels=labels)

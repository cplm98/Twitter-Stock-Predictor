from app.Twitter_Data import TwitterData
from app.DB_Manager import DBManager
from app.Stock_Data import StockData
import config

tweets = True
stocks = False

db = DBManager(r'C:\Projects\Twitter Stock Predictor\Twitter-Stock-Predictor\app\DB\database.db')
db.create_tables()

if tweets:
    twitter = TwitterData(config.twitter_consumer_key, config.twitter_consumer_secret, config.twitter_access_token,
                          config.twitter_access_token_secret, config.aylien_app_id, config.aylien_api_key)
    twitter.twitter_search('TSLA', 25)  # I think I run into aylien rate limits if I do more than 25 at a time
    twitter.clean_data()
    #db.store_tweet(twitter.twitter_data_list)

if stocks:
    stock = StockData("TSLA", "15min")
    stock.clean_stock_data(stock.get_stock_data())
    print(stock.data_list)
    db.store_stock_data(stock.data_list)

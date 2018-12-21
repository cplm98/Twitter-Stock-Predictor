import tweepy
from app import Sentiment_Analysis as sa
from app.DB_Manager import DBManager
import config

# think about maybe having a list of keywords to search through
# also tweets from the company itself
# also going to have to figure out ways to filter the results based on number of followers of the person who tweeted
# and generating a weighting of some sort


class TwitterData:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, ay_app_id, ay_api_key):
        self.sentiment_analysis = sa.SentimentAnalysis(ay_app_id, ay_api_key)
        self.twitter_data_list = []
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    # this just searches using a keyword
    def twitter_search(self, kw, count):
        self.search_results = self.api.search(q=kw, count=count, tweet_mode='extended')

    # gets relevant data from search result and add it to the data list
    def clean_data(self):
        for result in self.search_results:
            tweet_body = result.full_text
            time_stamp = str(result.created_at)
            tweet_id = result.id_str
            user_id = result.user.id_str
            username = self.api.get_user(user_id).screen_name
            #print("\n", time_stamp)
            retweets = int(result.retweet_count)
            favourites = int(result.favorite_count)
            verified = result.user.verified
            followers = result.user.followers_count
            polarity_confidence = self.sentiment_analysis.analyse(tweet_body)
            self.twitter_data_list.append((time_stamp, tweet_id, user_id, username, tweet_body, retweets, favourites, verified, followers, polarity_confidence))

            print("\n", tweet_body)


twitter = TwitterData(config.twitter_consumer_key, config.twitter_consumer_secret, config.twitter_access_token,
                      config.twitter_access_token_secret, config.aylien_app_id, config.aylien_api_key)
twitter.twitter_search('TSLA', 25)  # I think I run into aylien rate limits if I do more than 25 at a time
twitter.clean_data()
db = DBManager(r'C:\Projects\Twitter Stock Predictor\Twitter-Stock-Predictor\app\DB\database.db')
db.create_tables()
db.store_tweet(twitter.twitter_data_list)




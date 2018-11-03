import tweepy
import Sentiment_Analysis as sa

consumer_key = 'e20lS17XD24p34Rkip05M1XVK'
consumer_secret = 'Ztzyj6uL3R9ZjnOlbBQb2BJXoA7e3shrFH4cWwjkmTakBAiwDa'

access_token = '926753834-rE0JqvStEzQG7Xb8DwsZgM9bhxz3BQnGET7f4Brl'
access_token_secret = 'LvQO2gCWcEvqfZephAjuOZYdE2Hd4BYrUDhcVAMAIQ5VO'

app_id = 'd1c45467'
api_key = 'c55e70ee5c6921d841acf19db193c87b'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)
#
# search_results = api.search(q='tesla', count=100, tweet_mode='extended')  # filter by language too to improve sentiment analysis

# think about maybe having a list of keywords to search through
# also tweets from the company itself
# also going to have to figure out ways to filter the results based on number of followers of the person who tweeted
# and generating a weighting of some sort

# for i in search_results:
#     print(i.full_text, '\n')


class TwitterData:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.twitter_data_list = []
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    # this just searches using a keyword
    def twitter_search(self, kw, count):
        self.search_results = self.api.search(q=kw, count=count, tweet_mode="extended")

    # gets relevant data from search result and add it to the data list
    def clean_data(self):
        sentiment_analysis = sa.SentimentAnalysis(app_id, api_key)
        for result in self.search_results:
            tweet_body = result.full_text
            print(tweet_body)
            retweets = int(result.retweet_count)
            favourites = int(result.favorite_count)
            verified = result.user.verified
            followers = result.user.followers_count
            polarity_confidence = sentiment_analysis.analyse(tweet_body)
            self.twitter_data_list.append((tweet_body, retweets, favourites, verified, followers, polarity_confidence))


twitter = TwitterData(consumer_key, consumer_secret, access_token, access_token_secret)
twitter.twitter_search('TSLA', 50)
twitter.clean_data()
print(twitter.twitter_data_list)

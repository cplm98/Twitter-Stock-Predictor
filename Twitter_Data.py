import tweepy


consumer_key = 'e20lS17XD24p34Rkip05M1XVK'
consumer_secret = 'Ztzyj6uL3R9ZjnOlbBQb2BJXoA7e3shrFH4cWwjkmTakBAiwDa'

access_token = '926753834-rE0JqvStEzQG7Xb8DwsZgM9bhxz3BQnGET7f4Brl'
access_token_secret = 'LvQO2gCWcEvqfZephAjuOZYdE2Hd4BYrUDhcVAMAIQ5VO'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

search_results = api.search(q='tesla', count=100, tweet_mode='extended')  # filter by language too to improve sentiment analysis

# think about maybe having a list of keywords to search through
# also tweets from the company itself
# also going to have to figure out ways to filter the results based on number of followers of the person who tweeted
# and generating a weighting of some sort

for i in search_results:
    print(i.full_text, '\n')

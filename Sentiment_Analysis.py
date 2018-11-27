from aylienapiclient import textapi

app_id = 'd1c45467'
api_key = 'c55e70ee5c6921d841acf19db193c87b'


class SentimentAnalysis:
    # initializes session object using keys
    def __init__(self, app_id, api_key):
        self.client = textapi.Client(app_id, api_key)

    # takes in tweet and returns positive or negative confidence
    def analyse(self, tweet_text):
        sentiment = self.client.Sentiment(tweet_text)
        if sentiment['polarity'] == 'neutral':
            polarity_confidence = 0
        if sentiment['polarity'] == 'negative':
            polarity_confidence = int(100*(sentiment['polarity_confidence'] * -1))
        else:
            polarity_confidence = int(100*sentiment['polarity_confidence'])
        return polarity_confidence

# analysis = SentimentAnalysis(app_id, api_key)
# print(analysis.analyse('John is a mediocre football player'))
# looks pretty usable, this should be fun
# output = {'polarity_confidence': 0.9580259323120117, 'polarity': 'positive', 'subjectivity': 'subjective', 'subjectivity_confidence': 0.6145903344515379, 'text': 'John is a great football player'}

from aylienapiclient import textapi

app_id = 'd1c45467'
api_key = 'c55e70ee5c6921d841acf19db193c87b'

client = textapi.Client(app_id, api_key)

sentiment = client.Sentiment({'text': 'John is a great football player'})

print(sentiment)


# looks pretty usable, this should be fun
# output = {'polarity_confidence': 0.9580259323120117, 'polarity': 'positive', 'subjectivity': 'subjective', 'subjectivity_confidence': 0.6145903344515379, 'text': 'John is a great football player'}

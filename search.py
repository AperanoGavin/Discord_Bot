import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TWITTER)

id = "793961648"

response = client.get_users_tweets(id )

print(response)
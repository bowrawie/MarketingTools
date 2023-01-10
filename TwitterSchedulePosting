import tweepy
import schedule
import time

# Twitter API credentials
consumer_key = "CONSUMERKEY"
consumer_secret = "SECRETKEY"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet():
    # The message you want to tweet
    message = "Hello, Twitter!"
    # Send the tweet
    api.update_status(message)
    print("Tweeted: " + message)

# Schedule the tweet to be sent at a specific time
schedule.every().day.at("10:30").do(tweet)
schedule.every().day.at("17:00").do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

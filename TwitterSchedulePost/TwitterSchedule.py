import tweepy
import schedule
import time

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet():
    # The message you want to tweet
    message = "Hello, world!"
    # Send the tweet
    api.update_status(message)
    print("Tweeted: " + message)

# Schedule the tweet to be sent at a specific time
schedule.every().day.at("10:30").do(tweet)
schedule.every().day.at("17:00").do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

import tweepy
import requests

consumer_key = "qEkMcTsYo4Mt4eoaXs0oMagq8"
consumer_secret_key = "ErUWC4AGZcZn80Mbj4V3haGjA2x1cjMDfMNooOdBYFjceKEsx3"
access_token = "873550294310940672-bwL3XoaNfA4Q5vQtTrB7yCDAnTg3Ecp"
access_token_secret = "HwXvpl90z4UcwlkpgvuRxuNWM4gj8HujShjjst5uIOpYR"


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def tweet(new_post):
    api = authenticate()
    api.update_status(new_post)

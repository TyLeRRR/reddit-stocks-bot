import tweepy
import requests

consumer_key = **********
consumer_secret_key = *********
access_token = *********
access_token_secret = *********


def authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def tweet(new_post):
    api = authenticate()
    api.update_status(new_post)

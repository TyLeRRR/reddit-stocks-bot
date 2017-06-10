import praw
import json
import requests
import requests.auth
import time
import auth

access_token = auth.get_access_token()


def get_hot_topic():
    headers = {"Authorization": "bearer " + access_token, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.get("https://oauth.reddit.com/r/stocks/hot", headers=headers)
    print response.json()

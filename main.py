import praw
import json
import requests
import requests.auth
import time
import auth


def get_hot_topic(token):
    headers = {"Authorization": "bearer " + token, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.get("https://oauth.reddit.com/r/stocks/hot", headers=headers)
    temp_response = response.json()

    for object in temp_response['data']['children']:
        id = object['data']['id']
        save_post_id(id)


def save_post_id(post_id):
    file = open('post_ids.txt', 'r+')

    if post_id in file.read():
        print "Current id already exists"
    else:
        print "Writing id :" + post_id + " into file"
        file.write("%s\n" % post_id)
    file.close()

get_hot_topic(auth.get_access_token())


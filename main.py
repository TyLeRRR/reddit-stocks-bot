import praw
import json
import requests
import requests.auth
import time
import auth
import tweet


def get_hot_topic(token):
    headers = {"Authorization": "bearer " + token, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.get("https://oauth.reddit.com/r/stocks/hot", headers=headers)
    temp_response = response.json()

    for child in temp_response['data']['children']:
        child_data = child['data']
        id = child_data['id']
        if save_post_id(id):
            tweet.tweet(child_data['title'] + " " + child_data['url'])


def save_post_id(post_id):
    file = open('post_ids.txt', 'r+')

    if post_id in file.read():
        print "Current id already exists"
        return False
    else:
        print "Writing id :" + post_id + " into file"
        file.write("%s\n" % post_id)
        return True
    file.close()

while True:
    get_hot_topic(auth.get_access_token())
    time.sleep(300)
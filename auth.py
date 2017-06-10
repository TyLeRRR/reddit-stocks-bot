import requests

username = "Ty1eRRR"
password = "t3pdygE264C2hCj7"
app_client_ID = "n2Cyar-l0rGPTg"
app_client_secret = "BrYJBt6nLKOynK9ahrRKRJo90C4"


def get_access_token():
    client_auth = requests.auth.HTTPBasicAuth(app_client_ID, app_client_secret)
    post_data = {"grant_type": "password", "username": username, "password": password}
    headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data,
                             headers=headers)
    response_in_json = response.json()

    access_token = response_in_json['access_token']

    return access_token.encode('utf-8')

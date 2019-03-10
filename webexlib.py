import requests
import json
from api_key import api_key

url = "https://api.ciscospark.com/v1/"
headers = {"Authorization": "Bearer " + api_key}


def get_room_ids(url, headers):
    response = json.loads(requests.get(url + "rooms", headers=headers).text)['items']

    roomids = []

    for i in response:
        roomids.append(i['id'])

    return roomids

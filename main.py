from multiprocessing import Pool
import requests
import json
from api_key import api_key
import datetime
import webexlib

url = "https://api.ciscospark.com/v1/"
# This is the API URL, after which each endpoint is defined
headers = {"Authorization": "Bearer " + api_key}


# This is the authentication in the form of simple Bearer-key auth
# , and this needs to be refreshed every 12 hours from https://developer.webex.com


def send_memes():
    while 1:
        # Loop runs indefinitely
        if (datetime.date.today().weekday() == 0) and (datetime.time(hour=10, minute=0, second=0, microsecond=0)):
            # If today is the first day of the week (Monday) and the time is 10:00 AM
            for room in webexlib.get_room_ids(url, headers):
                # For every Room ID for this token
                kanye_rest = json.loads(requests.get("https://api.kanye.rest").text)['quote']
                # Get a new Kanye West quote (this is an API too, we can send a response from any other API to this API)
                # in a json format, then convert the json format to a dict, then assign the value corresponding to key
                # 'quote' to the variable kanye_rest
                message = {
                    "roomId": room,
                    "markdown": kanye_rest
                }
                # Important : the above is a payload that is passed to the POST request, and must be in the JSON format
                # All strings in this "dict" must be in double quotes adhering to JSON format

                requests.post("https://api.ciscospark.com/v1/messages?roomId=" + room, headers=headers,
                              data=message)
                # Simply posts the requests and takes all the above variables as params



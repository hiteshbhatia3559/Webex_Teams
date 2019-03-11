from multiprocessing import Process
import requests
import json
from api_key import api_key
import datetime
import webexlib
import time

url = "https://api.ciscospark.com/v1/"
# This is the API URL, after which each endpoint is defined
headers = {"Authorization": "Bearer " + api_key}


# This is the authentication in the form of simple Bearer-key auth
# , and this needs to be refreshed every 12 hours from https://developer.webex.com


def send_memes():
    while 1:
        # Loop runs indefinitely
        if datetime.date.today().weekday() == 0:
            # If today is the first day of the week (Monday
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
                print("Sent message " + message["markdown"] + " to " + room)

        time.sleep(86400)
        # If not Monday, sleep for one day


def send_close():
    while 1:
        # Loop runs indefinitely
        # If today is the fifth day of the week (Friday)
        if datetime.date.today().weekday() == 5:
            # Get the id of the room with name Screener, See webexlib.py for details
            room = webexlib.get_screener_roomid()
            # Get a new price from the Alpha Vantage API through the webexlib.py library and attach it to the payload
            message = {
                "roomId": room,
                "markdown": "MSFT's weekly price is " + str(webexlib.get_msft_price()),
            }
            # Important : the above is a payload that is passed to the POST request, and must be in the JSON format
            # All strings in this "dict" must be in double quotes adhering to JSON format
            requests.post("https://api.ciscospark.com/v1/messages?roomId=" + room, headers=headers, data=message)
            # Simply posts the requests and takes all the above variables as params
            print("Price sent to " + room)


# Multiprocessing implemented below
if __name__ == "__main__":
    try:
        # Purpose of this is not throw verbose errors
        p1 = Process(target=send_memes)
        # Initialize the first function asynchronously
        p2 = Process(target=send_close)
        # Initialize the second function asynchronously
        p1.start()
        p2.start()
        # Start both functions
        print("All okay, processes started\n")
        p1.join()
        p2.join()
        # Wait for both processes to complete before exiting the program
        # (will never happen unless an error is thrown from APIs)
    except:
        print("Not okay, contact Hitesh now")

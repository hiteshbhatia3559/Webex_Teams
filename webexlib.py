import requests
import json
from api_key import api_key
from alpha_vantage.timeseries import TimeSeries

# This is the library that wraps the API get methods as function calls

url = "https://api.ciscospark.com/v1/"
# API URL
headers = {"Authorization": "Bearer " + api_key}

#blank
print(json.loads(requests.get("https://api.ciscospark.com/v1/rooms", headers={"Authorization": "Bearer Yjk1ODE5ZGUtZDQ1Yi00YmRlLTg5ZGEtMTc0OGI4MTQ4YmY2ODU4ZDA3N2QtNDE4_PF84_consumer"}).text))

# Standard issue Bearer - Auth

def get_room_ids(url, headers):
    response = json.loads(requests.get(url + "rooms", headers=headers).text)['items']
    # Gets the JSON object which is a dict with every room,
    # then unpacks it to a dict and assigns the ['items'] key's values to response
    roomids = []
    # List of room ids to be returned
    for i in response:
        roomids.append(i['id'])
        # Find all room ids and return to a list for use later
    return roomids  # Return type is list


def get_msft_price():
    ts = TimeSeries(key="6N6NCHHOY72NXZ4T", output_format='pandas')
    # Initialize session with Alpha Vantage
    data, meta_data = ts.get_daily('MSFT')
    # Get all daily data for MSFT upto last close
    return data.tail(1)['4. close'].iloc[0]
    # Traverse the dataframe and get the value for the latest close, by getting the first tail row,
    # the close of the price and the price itself
    # Return type is float


def get_screener_roomid():
    roomids = get_room_ids(url, headers)
    # Get room ids, this is a function call to the first function in the lib
    needed_id = ""
    # Declare a variable that will store the id needed to send message to Screener space
    for id in roomids:

        response = json.loads(requests.get(url + "rooms/" + id, headers=headers).text)
        # Get the details of each room in roomids list
        if response['title'] == 'Screener':
            # if the name of the space is Screener
            needed_id = response['id']
            # Get the id of the space
    return needed_id
    # return the id

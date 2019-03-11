import requests
import json
from api_key import api_key
from alpha_vantage.timeseries import TimeSeries

url = "https://api.ciscospark.com/v1/"
headers = {"Authorization": "Bearer " + api_key}


def get_room_ids(url, headers):
    response = json.loads(requests.get(url + "rooms", headers=headers).text)['items']
    roomids = []
    for i in response:
        roomids.append(i['id'])
    return roomids


def get_msft_price():
    ts = TimeSeries(key="6N6NCHHOY72NXZ4T", output_format='pandas')
    data, meta_data = ts.get_daily('MSFT')
    return data.tail(1)['4. close'].iloc[0]

def get_screener_roomid():
    roomids = get_room_ids(url,headers)
    needed_id = ""
    for id in roomids:
        response = json.loads(requests.get(url+"rooms/"+id,headers=headers).text)
        if response['title'] == 'Screener':
            needed_id = response['id']
    return needed_id


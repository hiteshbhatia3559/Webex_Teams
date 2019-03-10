import requests
import json

api_key = "NjdhNGU4MmQtNjAwMy00ZTU3LWJmZmQtNjQxMjg2YTc0NzU3NWQzM2YwNmQtMTQx_PF84_consumer"

url = 'https://api.ciscospark.com/v1/'

headers = {"Authorization": "Bearer " + api_key}
#
# response = requests.get(url, headers=headers).text
#
# actual = json.loads(response)
#
# details = []
#
# for item in actual['items']:
#     details.append(item)
#
# roomId = details[2]['roomId']
#
# print(roomId)
# # Gets messages from room
# # response2 = json.loads(requests.get("https://api.ciscospark.com/v1/messages?roomId=" + roomId, headers=headers).text)
# #
# # print(response2)
#
# message = {
#   "roomId": roomId,
#   "markdown": "Hi"
# }
#
# response3 = requests.post("https://api.ciscospark.com/v1/messages?roomId=" + roomId,headers=headers,data=message)


import requests
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import Request, urlopen
import numpy as np
from bs4 import BeautifulSoup
import ssl
import json

token = "f63c928ff63c928ff63c928fc0f6571423ff63cf63c928fab1c741f053681679d4471a5"
id = "7046828"

URL = "https://api.vk.com/method/users.get"

PARAMS = {'user_id': 184058947,'v': 5.95, 'access_token': token, "fields": "city,bdate,sex,last_seen,counters,relation"}

r = requests.get(url = URL, params = PARAMS)
data = r.json()
# print(data['response'])


URL1 = "https://api.vk.com/method/friends.get"
PARAMS1 = {"user_id": 184058947, "v": 5.95, "access_token": token, "fields": "count"}

r1 = requests.get(url = URL1, params = PARAMS1)
data1 = r1.json()
json_string = json.dumps(data)
json_string = json_string.replace("[", "")
json_string = json_string.replace("]", "")
data = json.loads(json_string)
user = {
    "name": data['response']["first_name"],
    "surname": data['response']["last_name"],
    "sex": data['response']["sex"],
    "city": data['response']['city']['title'],
    "last_seen": data['response']["last_seen"]['time'],
    "pages": data['response']["counters"]['pages'],
    "friends": data1['response']["count"],
    "bdate": data['response']['bdate']
}
print(user)

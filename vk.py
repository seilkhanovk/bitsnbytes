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

# https://api.vk.com/method/users.get?user_id=166404213&v=5.95&access_token=f63c928ff63c928ff63c928fc0f6571423ff63cf63c928fab1c741f053681679d4471a5

URL = "https://api.vk.com/method/users.get"

PARAMS = {'user_id': 184058947,'v': 5.95, 'access_token': token, "fields": "city,bdate,sex,verified,contacts,site,education,last_seen,followers_count,counters,relation,personal,activities,interests,music,movies,tv,books,games"}

r = requests.get(url = URL, params = PARAMS)
data = r.json()
print(data['response'])

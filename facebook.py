
import requests
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import Request, urlopen
import numpy as np
from bs4 import BeautifulSoup
import ssl
import json

token = "EAAISTG5jF6cBAPdKUYXrJMS2bHQbn9MPKgCglxoXS5CSeRvkg9juZCNYS8bnmVZCvDghdIebhcXLRXkA6kTQgDqkWKbHPKWFYG9uMr7bAQSKpJuWWqi6i49qBzVd02q4qdGMQjnpr88Sfcoss3wqecWhMQTnY8JoXKwmCekQZDZD"

friends = "https://graph.facebook.com/v2.9/me/friends?access_token="+token
me = "https://graph.facebook.com/v2.9/me?access_token="+token
search = "https://graph.facebook.com/v2.9/search?q=mark zukerberg&type=user&access_token="+token
r = requests.get(url = search)
data = r.json()
print(data)

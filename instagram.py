#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
import ssl
import json

req = Request('https://www.ninjalitics.com/rrm777.html', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
data = soup.find_all('h3', attrs={'style': 'color: white; font-size: 16px; margin-bottom:5px; color:#fff; font-size: 14px;'})
print(data)

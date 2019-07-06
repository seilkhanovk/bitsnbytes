from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import ssl

username='rrm777'
browser = webdriver.Chrome('/Users/kuanysh/Desktop/chromedriver')
browser.get('https://www.instagram.com/'+username+'/?hl=en')

Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight/1.5);")
links=[]
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
script = body.find('span')
for link in script.findAll('a'):
     if re.match("/p", link.get('href')):
         links.append('https://www.instagram.com'+link.get('href'))
#sleep time is required. If you don't use this Instagram may interrupt the script and doesn't scroll through pages
time.sleep(5)
Pagelength = browser.execute_script("window.scrollTo(document.body.scrollHeight/1.5, document.body.scrollHeight/3.0);")
source = browser.page_source
data=bs(source, 'html.parser')
body = data.find('body')
script = body.find('span')
for link in script.findAll('a'):
     if re.match("/p", link.get('href')):
         links.append('https://www.instagram.com'+link.get('href'))

print(links)

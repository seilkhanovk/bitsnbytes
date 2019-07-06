from flask import Flask, jsonify
from flask import request
import requests
import urllib.request
import urllib.parse
import urllib.error
from urllib.request import Request, urlopen
import numpy as np
from bs4 import BeautifulSoup
import ssl
import json
import re
app = Flask(__name__)

def getInsta(user):
    url = 'https://www.ninjalitics.com/' + user + ".html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    # instagram user info

    data = soup.find_all('h3', attrs={'style': 'color: white; font-size: 16px; margin-bottom:5px; color:#fff; font-size: 14px;'})
    t1 = str(data[0])
    r1 = re.findall(r'\d+', t1)

    t2 = str(data[1])
    r2 = re.findall(r'\d+', t2)
    r3 = ""
    if len(data)>2:
        t3 = str(data[2])
        r3 = re.findall(r'\d+', t3)
        print(" Average Likes", r1[-2], "\n", "Average Comments", r2[-2], "\n", "Average Views", r3[-2])
    else :
        print(" Average Likes", r1[-2], "\n", "Average Comments", r2[-2], "\n")

    data1 = soup.find_all('script')
    t4 = str(data1[11])
    r4 = re.findall(r'\d+', t4)
    print(" Followers", r4[0], "\n", "Following", r4[1], "\n", "Posts", r4[2])



    # instagram user photo


    data2 = soup.find_all('img', attrs={'data-aos': 'zoom-in'})
    t5 = str(data2[0])
    pos1 = t5.find("https")
    pos2 = t5.find("style") - 2
    logoUrl = t5[pos1:pos2]
    print(logoUrl)

    inst = {
        'followers': r4[0],
        'following': r4[1],
        'posts': r4[2],
        'avg_likes': r1[-2],
        'avg_comments': r2[-2],
        'avg_views': r3[-2],
        'img': logoUrl
    }
    return inst

@app.route('/api', methods=['POST'])
def create_task():
    user = request.json['insta']
    instaInfo = getInsta(user)
    return jsonify(instaInfo)

if __name__ == '__main__':
    app.run(debug=True)

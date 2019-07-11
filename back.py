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
import pandas as pd
import pickle as p
app = Flask(__name__)

def getInsta(user):
    url = 'https://www.ninjalitics.com/' + user + ".html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')


    # instagram user info


    data = soup.find_all('h3', attrs={'style': 'color: white; font-size: 16px; margin-bottom:5px; color:#fff; font-size: 14px;'})
    t1 = str(data[0])
    pos1 = t1.find('>') + 2
    pos2 = t1.find("<",pos1,len(t1))
    r1 = t1[pos1:pos2]
    r1 = r1.replace(" ", "")
    r1 = r1.replace(",", "")
    print(r1, "\n")
    # r1 = re.findall(r'\d+', t1)

    t2 = str(data[1])
    r2 = re.findall(r'\d+', t2)

    if len(data)>2:
        t3 = str(data[2])
        pos1 = t3.find('>') + 2
        pos2 = t3.find("<",pos1,len(t1))
        r3 = t3[pos1:pos2]
        r3 = r3.replace(" ", "")
        r3 = r3.replace(",", "")
        # r3 = re.findall(r'\d+', t3)
        print(" Average Likes", r1, "\n", "Average Comments", r2[-2], "\n", "Average Views", r3)
    else :
        print(" Average Likes", r1, "\n", "Average Comments", r2[-2], "\n")

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
        'followers': str(r4[0]),
        'following': str(r4[1]),
        'posts': str(r4[2]),
        'avg_likes': str(r1),
        'avg_comments': str(r2[-2]),
        'avg_views': str(r3),
        'img': logoUrl
    }
    return inst

def getVk(userVk):

    token = "f63c928ff63c928ff63c928fc0f6571423ff63cf63c928fab1c741f053681679d4471a5"
    id = "7046828"

    URL = "https://api.vk.com/method/users.get"

    PARAMS = {'user_id': userVk,'v': 5.95, 'access_token': token, "fields": "city,bdate,sex,last_seen,counters,relation"}

    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    print(data['response'])


    URL1 = "https://api.vk.com/method/friends.get"
    PARAMS1 = {"user_id": userVk, "v": 5.95, "access_token": token, "fields": "count"}

    r1 = requests.get(url = URL1, params = PARAMS1)
    data1 = r1.json()
    json_string = json.dumps(data)
    json_string = json_string.replace("[", "")
    json_string = json_string.replace("]", "")
    data = json.loads(json_string)
    user = {
        "name": data['response']["first_name"],
        "surname": data['response']["last_name"],
        "sex": str(data['response']["sex"]),
        "city": data['response']['city']['title'],
        "last_seen": str(data['response']["last_seen"]['time']),
        "pages": str(data['response']["counters"]['pages']),
        "friends": str(data1['response']["count"]),
        "bdate": data['response']['bdate']
    }
    return user


@app.route('/api', methods=['POST'])
def create_task():
    userInsta = request.json['insta']
    userVk = request.json['vk']
    instaInfo = getInsta(userInsta)
    vkInfo = getVk(userVk)

    sex = int(vkInfo["sex"])
    bdate = 13
    friends = int(vkInfo["friends"])
    city = 10
    pages = int(vkInfo["pages"])
    lastSeen = 2
    followers = int(instaInfo["followers"])
    following = int(instaInfo["following"])
    posts = int(instaInfo["posts"])
    likes = int(instaInfo["avg_likes"])
    comments = int(instaInfo["avg_comments"])
    view = int(instaInfo["avg_views"])
    df = [sex, bdate, friends, city, pages, lastSeen, followers, following, posts, likes, comments, view]
    df = pd.Series(df)
    df = df.to_frame()
    df = df.transpose()
    prediction = model.predict(df)
    ans = {
        "insta": instaInfo,
        "vk": vkInfo,
        "model": str(prediction)
    }
    print(prediction)
    return jsonify(ans)

if __name__ == '__main__':
    modelfile = '/Users/kuanysh/Desktop/BitsNBytes/linear.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)

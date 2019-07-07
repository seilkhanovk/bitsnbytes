#!/usr/bin/env python
# coding: utf-8

# In[152]:


import pandas as pd


# In[153]:


import numpy as np


# In[154]:


df  = pd.read_csv('C:/Users/Rakhman/Anaconda3/dataBLE/soc.csv')
df.shape


# In[155]:


df


# In[156]:


#Преобразовываем данные по scoreboard (scorecards)

#VK

def sex_classifier(x):
    return 1
#не влияет

def married_classifier(x):
    if x==1:
        return 15
    if x==2:
        return 5
    return 10

def friends_classifier(x):
    if x>500:
        return 25
    if x>200:
        return 15
    if x>100:
        return 10
    if x>20:
        return 5
    return 0

def subscriptions_classifier(x):
    if x>30:
        return 10
    if x>20:
        return 15
    if x>5:
        return 5
    if x>1:
        return 1
    return 0


def city_classifier(x):
    if x=='Almaty':
        return 20
    if x=='Astana':
        return 15
    if x=='Shymkent':
        return 10
    return 5


def last_visit_classifier(x):
    if x==0:
        return 20
    if x==1:
        return 15
    if x<5:
        return 5
    if x<10:
        return 1
    return 0

#INSTAGRAM

def followers_classifier(x):
    if x>20000:
        return 50
    if x>2000:
        return 30
    if x>1000:
        return 25
    if x>500:
        return 20
    if x>200:
        return 15
    if x>100:
        return 10
    if x>30:
        return 5
    if x>1:
        return 1
    return 0

def followings_classifier(x):
    return followers_classifier(x)

def avg_views_classifier(x):
    return followers_classifier(x)

def posts_classifier(x):
    if x>50:
        return 40
    if x>30:
        return 30
    if x>10:
        return 20
    if x>5: 
        return 10
    if x>0:
        return 5
    return 0

def avg_likes_classifier(x):
    if x>100:
        return 30
    if x>500:
        return 25
    if x>200:
        return 20
    if x>100:
        return 15
    if x>50:
        return 10
    if x>5:
        return 5
    if x>0:
        return 1
    return 0

def avg_comments_classifier(x):
    if x>100:
        return 30
    if x>50:
        return 20
    if x>20:
        return 15
    if x>5:
        return 10
    if x>0:
        return 5
    return 0


# In[157]:


df['city'].fillna('Unknown')
for i in df.columns:
    if i!='vk_id' and i!='city' and i!='instagram_id':
        df[i].fillna(df[i].median())


# In[158]:


df['sex'] = df['sex'].apply(sex_classifier)
df['married'] = df['married'].apply(married_classifier)
df['friends'] = df['friends'].apply(friends_classifier)
df['subscriptions'] = df['subscriptions'].apply(subscriptions_classifier)
df['city'] = df['city'].apply(city_classifier)
df['last_visit'] = df['last_visit'].apply(last_visit_classifier)

df['followers'] = df['followers'].apply(followers_classifier)
df['followings'] = df['followings'].apply(followings_classifier)
df['posts'] = df['posts'].apply(posts_classifier)
df['avg_likes'] = df['avg_likes'].apply(avg_likes_classifier)
df['avg_comments'] = df['avg_comments'].apply(avg_comments_classifier)
df['avg_views'] = df['avg_views'].apply(avg_views_classifier)


# In[159]:


a = []
for i in range(df.shape[1]):
    a.append(0)
df['credit_score'] = pd.Series(a)
# df['credit_score'] = df['credit_score'] + df['married']
# df['credit_score'] = df['credit_score'] + df['followers']
df


# In[160]:


for i in df.columns:
    if i!='vk_id' and i!='instagram_id':
        df['credit_score'] = df['credit_score'] + df[i]
df['credit_score'] = df['credit_score']//2


# In[161]:


y_train = df['credit_score']
X_train = df.drop('credit_score',axis=1,inplace=True)


# In[162]:


X_train = df


# In[163]:


X_train.drop(['vk_id','instagram_id'],axis=1,inplace=True)


# In[164]:


#normalizing
y_train = y_train*1000//356
y_train #out of 1000


# In[165]:


from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)


# In[ ]:


linreg.predict(X_valid)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





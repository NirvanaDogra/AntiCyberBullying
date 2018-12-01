#!/usr/bin/env python

import string

badwords = []
for line in open("badwords.txt"):
    for word in line.split( ):
        badwords.append(word)

import tweepy
from tweepy import OAuthHandler

# set up api keys
consumer_key = "49iPPtb4tIVx20036qEwty0jp"
consumer_secret = "jl1ye0sPQtH4bbePY8on0YulyrkCSA0Ey6SBJhJJJUQNMvafCA"
access_token = "1046119739469320193-yCYX3fI2K1uUdVoWaW0LBMJV8dQIzI"
access_secret = "eX4QSonxwfrxoPpGzEkdDk76kHHQlj5apmvurOEKLGS1L"

# set up auth and api
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)     
api = tweepy.API(auth, wait_on_rate_limit=True)

for status in tweepy.Cursor(api.home_timeline).items(1):
    tweetText = status.text.encode("utf-8")
    tweetText = str(tweetText, errors='ignore')
    print ("tweet: "+ tweetText)
    # get rid of punctuation
    tweet = status.text
    tweet = "".join(l for l in tweet if l not in string.punctuation)
    tweet = tweet.lower()
    bullying = False
    for word in tweet.split(" "):
        if word in badwords:
            print ("bullying")
            api.update_status("@" + status.author.screen_name+"\n You should stop bullying people. (I am a bot in testing, don't take this too seriously)", status.id)
            bullying = True
            break
    if bullying == False:
        api.update_status("@" + status.author.screen_name+"\n Good job, you're not a bully! (I am a bot in testing, don't take this too seriously)", status.id)
        print ("not bullying")

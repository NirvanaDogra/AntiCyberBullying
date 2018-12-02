from __future__ import print_function
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import threading, time
from pprint import pprint

from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput


#If service instance provides API key authentication
service = ToneAnalyzerV3(version='2018-11-01',
                         url='https://gateway-syd.watsonplatform.net/tone-analyzer/api',
                         iam_apikey='J4a1j1p3o6zKwoSPqJwYQ_l40lNRU85DaTLrQFVKGfbq')





#################################3
cred = credentials.Certificate('C:/Users/Nirvan Dogra/PycharmProjects/TwitterAPI/simulation.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://simulation-1270b.firebaseio.com/'
})


while(1):

    result = db.reference('messages/msg').get()
    print(result)
    if result == "empty":
        print("null"+result)
        continue;

    ####################################333

    tone_input = result  #the value from db(firebase)


    #making  the call to analysis
    print("\ntone() example 1:\n")
    print(json.dumps(service.tone(tone_input, content_type="text/plain").get_result(), indent=2))
    data = (json.dumps(service.tone(tone_input, content_type="text/plain").get_result(), indent=2))

    with open('result.json', 'w+') as fp:
        fp.write(data)

    print("\n\n")
    with open('result.json') as f:
        data = json.load(f)
    pprint(data)


    with open('result.json') as f:
        found = ""
        for line in f:
            if "tone_name" in line:
                found = line
                break

    print("Your emotion are as follows")
    print(line)

    bully = "NO"
    if("Anger" in line):
        bully = "YES";
    elif("Sad" in line):
        bully = "NO";

    print(bully)



    root = db.reference('messages').update({'isCyberBullying': bully,
                                            'msg': "empty",
                                            "emotionType": line})

    print("end of execution ")
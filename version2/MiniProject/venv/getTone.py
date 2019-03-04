from __future__ import print_function
import json
import csv
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
cred = credentials.Certificate('chatting-2e9b2-firebase-adminsdk-j1nqm-fa749ae061.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://chatting-2e9b2.firebaseio.com/'
})

def GetValue(result):

        result = db.reference('Message').get()
        print(result)
        if result == "empty":
            print("null"+result)


        ####################################333

        tone_input = result  #the value from db(firebase)


        #making  the call to analysis
        print("\ntone() example 1:\n")
        print(json.dumps(service.tone(tone_input, content_type="text/plain").get_result(), indent=2))
        data = (json.dumps(service.tone(tone_input, content_type="text/plain").get_result(), indent=2))


        with open('result.json', 'w+') as fp:
            fp.write(data)

        from josnTocsv import convert;
        convert(result)
        print("\n\n")

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



        root = db.reference('chatting-2e9b2').update({'isCyberBullying': bully,
                                                'msg': "empty",
                                                "emotionType": line})

        ab=db.reference('isBullying').set(bully);

        #root = db.reference('isBully').post(bully);

        print("end of execution ")

with open("DataInput.txt", encoding="utf-8") as f:
    content = f.readlines()
    for i in range(0,len(content)):
        line=content[i]
        result = line[line.find(': ')+2:]
        print(result)
        print("#####")
        while(1):
            GetValue(result)
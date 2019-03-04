import json
import csv
from pprint import pprint

def convert(text):
    text=text[:-1]
    result=""
    with open('result.json', 'r') as f:
        result = json.load(f)


    pprint(result)
    line=result['document_tone']['tones']
    
    if(len(line)==0):return
    pprint(line[0])

    pprint(line[0]['score'])
    pprint(line[0]['tone_id'])
    pprint(line[0]['tone_name'])
    for i in (range(0,len(line))):
        list=[text, line[i]['score'], line[i]['tone_id'], line[i]['tone_name']]
        with open('test.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(list)

    csvFile.close()

text="Bhai  I am really  sorry\n"
convert(text)

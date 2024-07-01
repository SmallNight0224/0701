from flask import Flask, render_template
from urllib.request import urlopen
import ssl
import json

app = Flask(__name__)



@app.route('/')
def index():
    print('aa')  
    
    json_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-8D5AACAD-CC31-4143-BEEB-AF1ED9DD9B6C&format=JSON"
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urlopen(json_url)
    dict_example ={"city":[],"wx8":[],"maxt8":[],"mint8":[],"pop8":[]}
    list_example=[]
    data = response.read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        city = i['locationName']    # 縣市名稱
        wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
        maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
        mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
        ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
        pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
        print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')
        dict_example['city'].append(city)
        dict_example['wx8'].append(wx8)
        dict_example['maxt8'].append(maxt8)
        dict_example['mint8'].append(mint8)
        dict_example['pop8'].append(pop8)
        list_example.append(city)
    print(dict_example)
    return render_template('index.html',dict_example=dict_example)


if __name__ == '__main__':
    app.run()

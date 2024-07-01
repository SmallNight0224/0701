from urllib.request import urlopen
import ssl  # 解决步骤1
import json

json_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-8D5AACAD-CC31-4143-BEEB-AF1ED9DD9B6C&format=JSON"
ssl._create_default_https_context = ssl._create_unverified_context
response = urlopen(json_url)
data = response.read()
output = json.loads(data)
location=output['records']['location']

for i in location:
    print(f'{i}')

for i in location:
    city = i['locationName']    # 縣市名稱
    wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
    pop8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
    mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
    ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
    maxt8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
    print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')



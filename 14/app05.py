from urllib.request import urlopen
import ssl
import json

json_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/A-B0062-001?Authorization=CWA-8D5AACAD-CC31-4143-BEEB-AF1ED9DD9B6C&CountyName=%E8%87%BA%E6%9D%B1%E7%B8%A3"
ssl._create_default_https_context = ssl._create_unverified_context
response = urlopen(json_url)

data = response.read()
output = json.loads(data)

location=output['records']['locations']['location']

for i in location:
    print(f'{i}')


for i in location:
  with open('mydata.json', 'wb') as f:
    f.write(json.dumps(i).encode())
import urllib.request as req
import ssl,json,os
import openpyxl

# 空氣品質AQI
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=221974dd-667c-4243-b308-61b60bc29986&limit=1000&sort=ImportDate%20desc&format=JSON'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

request = req.Request(url, headers=header)

with req.urlopen(request) as f:
    result = f.read().decode('utf-8')

print(type(result))

json_datas = json.loads(result)

# print(type(json_datas))
# print(json_datas['records'])

for data in json_datas['records']:
    print(f'{data['sitename']}--{data['county']}: AQI {data['aqi']}')
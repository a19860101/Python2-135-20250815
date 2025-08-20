import urllib.request as req
import ssl,csv,os
import openpyxl

# 空氣品質AQI
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://data.taipei/api/dataset/4acb4911-0360-4063-808d-fcee629508b3/resource/893c2f2a-dcfd-407b-b871-394a14105532/download'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

request = req.Request(url, headers=header)

with req.urlopen(request) as f:
    result = f.read().decode('cp950')

# print(result)
# csv_datas = csv.reader(result)
csv_datas = csv.reader(result.splitlines())
# csv_datas = csv.DictReader(result)
# print(csv_datas)
#
#
for c in csv_datas:
    print(c)



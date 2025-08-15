import urllib.request as req

url = 'https://www.ptt.cc/bbs/index.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}
request = req.Request(url,headers=header)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

print(result)
print(res.closed)

# res.close()

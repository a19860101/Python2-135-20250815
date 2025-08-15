import urllib.request as req

url = 'https://www.ptt.cc/bbs/index.html'

request = req.Request(url)

res = req.urlopen(request)

result = res.read().decode('utf-8')

print(result)
import urllib.request as req
import bs4

url = 'https://www.ptt.cc/bbs/Baseball/index19886.html'

request = req.Request(url)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

html = bs4.BeautifulSoup(result,'html.parser')

# print(html.find('title'))
# print(html.find('a'))
# print(html.find_all('a'))
# print(html.find_all('span'))

# print(html.find_all('div',class_='b-ent'))

data = html.find_all('div',class_='r-ent')
# print(data)
for item in data:
    print(item.find('div',class_='title').text)
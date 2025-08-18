import urllib.request as req
import bs4

url = 'https://www.ptt.cc/bbs/Baseball/index19886.html'

request = req.Request(url)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

html = bs4.BeautifulSoup(result,'html.parser')

data = html.find_all('div',class_='r-ent')
# print(data)
with open('test.txt', 'a', encoding='utf-8') as f:
    for item in data:
        # print(item.find('div',class_='title').text)
        title = item.find('div',class_='title').a.text
        date = item.find('div',class_='date').text
        author = item.find('div',class_='author').text

        print(title)

        content = f'{date} -- {title} -- {author} \n'

        f.write(content)
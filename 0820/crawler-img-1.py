import urllib.request as req
import os
import bs4
import ssl

url = 'https://www.lccnet.com.tw/lccnet'
ssl._create_default_https_context = ssl._create_unverified_context

request = req.Request(url)

with req.urlopen(request) as f:
    result = f.read().decode('utf-8')

# print(result)

html = bs4.BeautifulSoup(result,'html.parser')

# print(html)

imgs = html.find_all('img')
# print(imgs)
for img in imgs:
    # print(img['src'])
    _ , ext = os.path.splitext(img['src'])
    imgname = os.path.basename(img['src'])
    print(imgname)
    os.makedirs('output',exist_ok=True)

    req.urlretrieve(f'https://www.lccnet.com.tw{img['src']}',f'output/{imgname}')
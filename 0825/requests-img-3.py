import os

import requests
import bs4
from urllib.parse import urljoin


url = 'https://www.vscinemas.com.tw/film/index.aspx'

req = requests.get(url, verify=False)

print(req)

data = req.text

html = bs4.BeautifulSoup(data, 'html.parser')

# print(html)

imgs = html.find_all('img')
# print(imgs)
# i=0
for i,img in enumerate(imgs):
    src = urljoin(url, img['src'])
    print(src)
    _,ext = os.path.splitext(img['src'])
    img_data = requests.get(src, verify=False)

    os.makedirs('movies', exist_ok=True)
    with open(f'movies/{i+1}{ext}','wb')as f:
        f.write(img_data.content)

    # i+=1

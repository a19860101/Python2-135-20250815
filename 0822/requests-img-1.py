import requests
import bs4
import os

url = 'https://www.tenlong.com.tw/'

res = requests.get(url)

result = res.text

html = bs4.BeautifulSoup(result,'html.parser')

imgs = html.find_all('img')
for idx,img in enumerate(imgs):
    # print(img)
    try:
        img_data = requests.get(img['src'])
        _,ext = os.path.splitext(img['src'])
        print(ext[:4])
        filename = os.path.basename(img['src'])
        # os.makedirs('images',exist_ok=True)
        # with open(f'images/{idx+1}{ext}','wb') as f:
        with open(f'images/{filename}','wb') as f:
            f.write(img_data.content)
    except Exception as e:
        print(e)
        pass
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
        # 去除某些檔案副檔名後面含有的其他參數
        ext = ext[:4]
        # 完整圖片路徑
        fullname = _+ext
        # filename = os.path.basename(img['src'])

        # 取得檔名+副檔名
        filename = os.path.basename(fullname)
        print(filename)
        os.makedirs('images',exist_ok=True)
        # with open(f'images/{idx+1}{ext}','wb') as f:
        with open(f'images/{filename}','wb') as f:
            f.write(img_data.content)
    except Exception as e:
        print(e)
        pass
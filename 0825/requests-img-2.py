import os
import requests

url = 'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&keyword=&currency=TWD&sort=prec&page=1&start=0&count=10'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

request = requests.get(url, headers=header, verify=False)

json_data = request.json()

for idx,data in enumerate(json_data['data']['data']):
    print(data['img_url_list'])
    for i, img in enumerate(data['img_url_list']):
        im = requests.get(img, verify=False)
        os.makedirs(f'images/{idx+1}', exist_ok=True)
        with open(f'images/{idx+1}/img-{i+1}.jpg', 'wb') as f:
            f.write(im.content)
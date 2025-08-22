import requests
import openpyxl
import os

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['行程','最高價','最低價','評價','評價人數'])

url = 'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&keyword=&currency=TWD&sort=prec&page=1&start=0&count=10'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}

res = requests.get(url,headers=header,verify=False)

result = res.json()

for item in result['data']['data']:
    print(item['name'])
    print('標題', item['name'])
    print('最高價', item['max_price'])
    print('最低價', item['min_price'])
    print('評論人數', item['rating_count'])
    print('平均', item['rating_star'])

    ws.append([item['name'],item['max_price'],item['min_price'],item['rating_star'],item['rating_count']])
os.makedirs('output',exist_ok=True)
wb.save('output/kkday.xlsx')


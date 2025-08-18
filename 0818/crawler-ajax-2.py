import urllib.request as req
import ssl,json,os
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['標題','最高價','最低價','評價','評價人數'])

ssl._create_default_https_context = ssl._create_unverified_context


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}
for i in range(10):
    url = f'https://www.kkday.com/zh-tw/category/ajax_get_category_product_list?productCategory=CATEGORY_019&keyword=&currency=TWD&sort=prec&page={i+1}&start=0&count=10'
    request = req.Request(url, headers=header)

    with req.urlopen(request) as res:
        result = res.read().decode('utf-8')


    json_data = json.loads(result)
    # print(json_data['data']['data'])
    for data in json_data['data']['data']:
        print('標題',data['name'])
        print('最高價',data['max_price'])
        print('最低價',data['min_price'])
        print('評論人數',data['rating_count'])
        print('平均',data['rating_star'])
        print('-----------------------------')
        ws.append([data['name'],data['max_price'],data['min_price'],data['rating_star'],data['rating_count']])

os.makedirs('output',exist_ok=True)
wb.save('output/kkday.xlsx')
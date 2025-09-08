import urllib.parse

import requests

page = input('請輸入頁數（每頁約20筆資料）:')
kw = input('請輸入搜尋關鍵字：')
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'referer': 'https://www.104.com.tw/'
}
kw = urllib.parse.quote(kw)
for p in range(int(page)):

    url = f'https://www.104.com.tw/jobs/search/api/jobs?area=6001001005&jobsource=joblist_search&keyword={kw}&mode=s&order=15&page={p + 1}&pagesize=20'

    # 'https://www.104.com.tw/jobs/search/api/jobs?area=6001001005&jobsource=joblist_search&keyword=%E8%A8%AD%E8%A8%88&mode=s&order=15&page=4&pagesize=20'


    res = requests.get(url, headers=header, verify=False)

    jsonfile = res.json()

    # print(jsonfile)
    print(len(jsonfile['data']))
    for job in jsonfile['data']:
        print(job['custName'])
        print(job['jobName'])
        if job['salaryLow'] == 0 and job['salaryHigh'] == 0 :
            print('面議')
        elif job['salaryHigh'] == 9999999:
            print(f'時薪{job['salaryLow']}',job['salaryHigh'] )
        else:
            print(job['salaryLow'],'~',job['salaryHigh'])

        print('------------------------------')
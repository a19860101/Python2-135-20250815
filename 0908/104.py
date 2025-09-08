import requests

page = input()
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'referer': 'https://www.104.com.tw/'
}

for p in range(int(page)):

    url = f'https://www.104.com.tw/jobs/search/api/jobs?area=6001001005&jobsource=joblist_search&keyword=python&mode=s&order=15&page={p + 1}&pagesize=20'



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
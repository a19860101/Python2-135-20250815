import urllib.request as req
import bs4
import openpyxl
import os

wb = openpyxl.Workbook()
ws = wb.active

os.makedirs('output',exist_ok=True)

ws.append(['人氣','日期','標題','作者'])

url = 'https://www.ptt.cc/bbs/Baseball/index19886.html'

request = req.Request(url)

with req.urlopen(request) as res:
    result = res.read().decode('utf-8')

html = bs4.BeautifulSoup(result,'html.parser')

data = html.find_all('div',class_='r-ent')
for item in data:
    # print(item.find('div',class_='title').text)
    title = item.find('div',class_='title').a.text
    date = item.find('div',class_='date').text
    author = item.find('div',class_='author').text
    nrec = item.find('div',class_='nrec').span.text
    ws.append([nrec, date, title, author])

wb.save('output/baseball.xlsx')

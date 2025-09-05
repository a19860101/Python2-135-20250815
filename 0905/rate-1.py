import bs4
import  requests

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

res = requests.get(url)

result = res.text

htmlfile = bs4.BeautifulSoup(result, 'html.parser')


us = htmlfile.select_one('tbody tr:nth-of-type(1) td:nth-of-type(3)').text
hkd = htmlfile.select_one('tbody tr:nth-of-type(2) td:nth-of-type(3)').text
yen = htmlfile.select_one('tbody tr:nth-of-type(8) td:nth-of-type(3)').text
print(us,hkd, yen)

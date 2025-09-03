import time

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://github.com/a19860101'

header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-TW,zh;q=0.9",
    "cache-control": "max-age=0",
    "if-none-match": "W/\"e8ecb1af84c4ceb23e43c8ec5c6bfba9\"",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "Cookie": "_octo=GH1.1.260781732.1756896646; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FTaipei; _device_id=d9645fac3438f51d6015ad1e94f294d8; saved_user_sessions=7856706%3AGxGQpZxloJFmNWVu1Ux_qsBfSpqzVp9UGgpObq6VJj5DCwSD; user_session=GxGQpZxloJFmNWVu1Ux_qsBfSpqzVp9UGgpObq6VJj5DCwSD; __Host-user_session_same_site=GxGQpZxloJFmNWVu1Ux_qsBfSpqzVp9UGgpObq6VJj5DCwSD; tz=Asia%2FTaipei; color_mode=%7B%22color_mode%22%3A%22light%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=a19860101; _gh_sess=tFx%2BKpoHJMwG%2BhJtmx1qistRSqRXQfKNfW1IXUAKpKmeAOwLFGDCtScCQUHomcnbF4%2BpQxyOCwX0OhUCbqg%2F8anhfiCYf3MLk5slKuLiQ9mTli4ZJmcJO9Wmw%2FAVTITB1NSoIJPi19Wi%2BuQeOUlOFt2vxW1W1mDLYYswzOZeNXg0sMoN2dhMLRf5wuZh2S3nrCVHVGJ7ZII212xkrauV3KUvTKiBj9R1ZDmthpLohduL4x8nhfT06qTc5wNXqM6Bt3Cp6g6ut6PZ5F44aTmaQk1buOc7%2FFADAzhpbA15Vi1CHH24H6z0z8QIYj9chjxAb9NYU3YZ9GrX1Z9Uvfzr2u1KfyF60tFVU7o9SLsnQoCZSzhRsXqcMBtFbguK%2BUsp49WvXCJ9x4WDHyw8gh1KhKvAFnmX5qywpgXGLcSVTw7pXcJqBgIzEx2d79KyW73HTXfehikN7%2B1eAs1Jpfs4RLXhLDpoJuxmC7x8nt2uq%2BLUer0QL%2FwfBy5gIy1q03BSNKPFFSNSpfo%3D--H5%2FJ3ZTAnV6tofw4--4bDbDOHURRiDBrEiMRbdJg%3D%3D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=header, verify=False)
# AppHeader-context-item-label

result = res.text

htmlfile = bs4.BeautifulSoup(result, 'html.parser')

# username = htmlfile.find('span', class_='AppHeader-context-item-label')
# print(htmlfile)
# print(username)

cookies = {}

for cookie in header['Cookie'].split(';'):
    if '=' in cookie:
        name, value = cookie.strip().split('=')
        cookies[name] = value

# print(header['Cookie'].split(';'))
print(cookies)

driver = webdriver.Chrome()
driver.get(url)
# driver.add_cookie(cookies)


for name, value in cookies.items():
    try:
        driver.add_cookie({
            'name': name,
            'value': value,
        })
    except:
        pass

driver.refresh()
time.sleep(10)
# t = driver.find_element(By.CLASS_NAME,'AppHeader-context-item-label')

# print(t)

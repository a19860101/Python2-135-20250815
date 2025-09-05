import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = 'https://www.cwa.gov.tw/V8/C/W/week.html'

driver.get(url)
driver.maximize_window()

time.sleep(5)

county = driver.find_element(By.CSS_SELECTOR,'tbody:nth-of-type(1) .heading_3')

temps = driver.find_elements(By.CSS_SELECTOR,'tbody:nth-of-type(1) .day td[headers*="day"]')

# print(temps)
print(county.text,'一周天氣')
for temp in temps:
    t = temp.find_element(By.CSS_SELECTOR,'p .is-active')
    print(temp.text)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'

driver.get(url)
driver.maximize_window()

reload = driver.find_element(By.CLASS_NAME, 'click_reload')

reload.click()

time.sleep(2)


# us = driver.find_element(By.XPATH, '//*[@id="ie11andabove"]/div/table/tbody/tr[1]/td[3]')
# jp = driver.find_element(By.XPATH, '//*[@id="ie11andabove"]/div/table/tbody/tr[8]/td[3]')
# us = driver.find_element(By.CSS_SELECTOR, 'tbody tr:nth-of-type(1) td:nth-of-type(3)')
# jp = driver.find_element(By.CSS_SELECTOR, 'tbody tr:nth-of-type(8) td:nth-of-type(3)')
# print(us.text, jp.text)

r = driver.find_elements(By.CSS_SELECTOR,'tbody tr')

for item in r:
    country = item.find_element(By.CSS_SELECTOR,'td:nth-of-type(1)')
    rate1 = item.find_element(By.CSS_SELECTOR,'td:nth-of-type(2)')
    rate2 = item.find_element(By.CSS_SELECTOR,'td:nth-of-type(3)')
    print(country.text,rate1.text,rate2.text)
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# wb = openpyxl.Workbook()
# ws = wb.active

# ws.append(['商品名稱','價格','商品連結'])
driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/'
driver.get(url)
driver.maximize_window()

link1 = driver.find_element(By.LINK_TEXT, '男款')
link1.click()
time.sleep(2)
link2 = driver.find_element(By.LINK_TEXT, '運動裝備')
link2.click()

time.sleep(10)

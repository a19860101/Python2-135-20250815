import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

ws.append(['商品名稱','價格','商品連結'])
driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/w/mens-training-gym-shoes-58jtoznik1zy7ok'
driver.get(url)
driver.maximize_window()

pcount = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1500)')
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME, 'product-card')
    if pcount == len(products):
        break
    pcount = len(products)

print(pcount)
i=0
for product in products:
    ptitle = product.find_element(By.CLASS_NAME, 'product-card__title').text
    pprice = product.find_element(By.CLASS_NAME, 'product-price').text
    plink = product.find_element(By.CLASS_NAME, 'product-card__link-overlay').get_attribute('href')
    # product-card__link-overlay
    # print(f'{ptitle}:{pprice}')
    ws.append([ptitle,pprice,plink])
    ws[f'C{i+2}'].hyperlink = plink
    i+=1

os.makedirs('output', exist_ok=True)

wb.save(f'output/nike.xlsx')

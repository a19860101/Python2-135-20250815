import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


url = 'https://www.nike.com/tw/w/mens-basketball-shoes-3glsmznik1zy7ok'
driver.get(url)
driver.maximize_window()
# driver.execute_script('window.scrollTo(0, 3000)')
# time.sleep(5)

# for i in range(3):
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1500)')
#     time.sleep(5)

# products = driver.find_elements(By.CLASS_NAME, 'product-card')
# print(len(products))
# time.sleep(5)

pcount = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1500)')
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME, 'product-card')
    if pcount == len(products):
        break
    pcount = len(products)


print(pcount)
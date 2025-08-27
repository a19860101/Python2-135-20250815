import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


url = 'https://www.nike.com/tw/w/mens-shoes-nik1zy7ok'
driver.get(url)

# driver.execute_script('window.scrollTo(0, 3000)')
# time.sleep(5)

for i in range(3):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)

products = driver.find_elements(By.CLASS_NAME, 'product-card')
print(len(products))
time.sleep(5)
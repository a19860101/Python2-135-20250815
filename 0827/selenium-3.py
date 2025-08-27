import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/w/mens-shoes-nik1zy7ok'
driver.get(url)

driver.maximize_window()

# product-card
# product-card__hero-image css-1fxh5tw
# product-card__title
# product-price

products = driver.find_elements(By.CLASS_NAME,'product-card')

# print(products)

for product in products:
    # print(product.find_element(By.CLASS_NAME,'product-card__title').text)
    ptitle = product.find_element(By.CLASS_NAME,'product-card__title').text
    pprice = product.find_element(By.CLASS_NAME,'product-price').text
    print(f'{ptitle}:{pprice}')



# time.sleep(5)
driver.close()
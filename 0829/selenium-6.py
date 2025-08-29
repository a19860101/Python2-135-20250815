import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/w/mens-basketball-shoes-3glsmznik1zy7ok'
driver.get(url)
driver.maximize_window()
# loader-bar
pcount = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1200)')

    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'loader-bar'))
            # EC.invisibility_of_element((By.CLASS_NAME, 'loader-bar'))
        )
    except Exception as e:
        print(e)

    products = driver.find_elements(By.CLASS_NAME, 'product-card')
    if pcount == len(products):
        break
    pcount = len(products)

time.sleep(5)
print(pcount)
for product in products:
    print(product.find_element(By.CLASS_NAME, 'product-card__title').text)
driver.close()

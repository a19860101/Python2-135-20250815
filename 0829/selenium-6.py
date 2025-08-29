import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = 'https://www.nike.com/tw/w/mens-training-gym-shoes-58jtoznik1zy7ok'
driver.get(url)
driver.maximize_window()
# loader-bar

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight-1000)')

    try:
        WebDriverWait(driver, 10).until(
            # EC.invisibility_of_element_located(By.CLASS_NAME, 'loader-bar')
            EC.invisibility_of_element((By.CLASS_NAME, 'loader-bar'))
        )
    except Exception as e:
        print(e)
        driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = 'https://www.cwa.gov.tw/V8/C/W/week.html'

driver.get(url)
driver.maximize_window()

time.sleep(5)

county = driver.find_elements(By.CSS_SELECTOR,'tbody')

for c in county:
    name = c.find_element(By.CSS_SELECTOR,'.heading_3')
    print(name.text)
    temps = c.find_elements(By.CSS_SELECTOR, '.day td[headers*="day"]')
    for temp in temps:
        t = temp.find_element(By.CSS_SELECTOR, 'p .is-active')
        print(temp.text)


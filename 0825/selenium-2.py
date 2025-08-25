from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get('https://google.com')
time.sleep(3)
driver.maximize_window()
time.sleep(3)
search = driver.find_element(By.CLASS_NAME, 'gLFyf')
time.sleep(3)
# search.send_keys('python',Keys.ENTER)
search.send_keys('p')
time.sleep(3)
search.send_keys('y')
time.sleep(2)
search.send_keys('t')
time.sleep(1)
search.send_keys('h')
time.sleep(1.2)
search.send_keys('o')
time.sleep(2)
search.send_keys('n')

time.sleep(2)

search.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()

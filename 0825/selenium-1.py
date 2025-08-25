from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://google.com')

driver.maximize_window()

driver.save_screenshot('google.png')

driver.get('https://www.tenlong.com.tw/')

driver.save_screenshot('tenlong.png')

time.sleep(2)

driver.close()

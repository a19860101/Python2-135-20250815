import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = 'https://www.uniqlo.com/tw/zh_TW/'
driver.get(url)
driver.maximize_window()

search = driver.find_element(By.CLASS_NAME,'li-search')
search.click()

time.sleep(3)

men = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div[3]/div[2]/div[1]/span[2]')
men.click()

time.sleep(3)

# rank = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[27]/div/span')
rank = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div[26]/div/span')
rank.click()

time.sleep(20)
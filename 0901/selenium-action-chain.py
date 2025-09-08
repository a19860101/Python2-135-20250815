import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = 'https://www.uniqlo.com/tw/zh_TW/'

driver.get(url)
driver.maximize_window()

action = ActionChains(driver)

search = driver.find_element(By.CLASS_NAME,'li-search')
account = driver.find_element(By.CSS_SELECTOR,'li>.icon-account')

# action.click(search).perform()

# action.move_to_element(search).click().perform()

# action.click(account).perform()
action.click(account).perform()
time.sleep(10)

# reg = driver.find_element(By.CLASS_NAME,'panel-right')

# action.move_to_element_with_offset(reg,0,20).click().perform()
# 右鍵
# action.move_to_element_with_offset(reg,0,20).context_click().perform()

login = driver.find_element(By.NAME, 'contactEmail')
pw = driver.find_element(By.NAME,'password')
enter = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div/div[2]/div/div/div[2]/form/div[3]/div/button')
action.click(login).send_keys('a19860101@gmail.com').pause(5).click(pw).send_keys('Lcc19860101').click(enter).perform()
time.sleep(10)




import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = 'https://www.taiwanlottery.com/lotto/result/lotto649'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()


time.sleep(5)
select = driver.find_element(By.ID, 'date_picker_98')
month = driver.find_element(By.CSS_SELECTOR, 'td[aria-label="8 月"]')
search = driver.find_element(By.XPATH,'//*[@id="__nuxt"]/main/div[1]/div[2]/div/nav/div[4]/button')

print(select)

# action = ActionChains(driver)
# action.click(select).pause(2).click(month).pause(2).click(search).perform()
#
# time.sleep(5)
#
# driver.execute_script('window.scrollTo(0, 500)')
#
# time.sleep(10)



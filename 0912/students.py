import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
url = 'https://member.lccnet.com.tw/signout/LearningRecord.aspx'
# http://attend.lccnet.com.tw/TeamRecord.aspx
driver = webdriver.Chrome()
driver.get(url)
action = ActionChains(driver)

driver.maximize_window()

time.sleep(5)

student_id = ''

# user = driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/form/div/div[2]/div/div[1]/div[2]/div[2]/input')
user = driver.find_element(By.NAME,'關鍵字')
enter = driver.find_element(By.CLASS_NAME,'profileSave')

print(user)

action.send_keys_to_element(user,student_id).pause(5).click(enter).pause(10).perform()





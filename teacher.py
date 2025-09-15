import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url = 'https://teacher.lccnet.com.tw/Message'

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

action = ActionChains(driver)

user = driver.find_element(By.NAME,'Account')
pw = driver.find_element(By.NAME,'Password')
login = driver.find_element(By.ID,'login_btn')


(
    action.
    send_keys_to_element(user,'a19860101@gmail.com').
    send_keys_to_element(pw,'a19860101@gmail.com').
    click(login).
    perform()
)


time.sleep(5)
gotocourse = driver.find_element(By.XPATH,'//*[@id="course_slider"]/div[1]/div/div/div/div/div[5]/a')

(
    action.
    click(gotocourse).
    pause(5).
    perform()
)

create_zoom = driver.find_element(By.LINK_TEXT, '建立教室')
create_zoom.click()
time.sleep(5)

create_zoom_confirm = driver.find_element(By.CLASS_NAME, 'zoom-button')
create_zoom_confirm.click()
time.sleep(30)

start_course = driver.find_element(By.LINK_TEXT,'進入教室')
start_course.click()
time.sleep(5)


# (
#     action.
#     click(create_zoom).
#     pause(5).
#     click(create_zoom_confirm).
#     pause(15).
#     click(start_course).
#     pause(10).
#     perform()
# )

time.sleep(10)



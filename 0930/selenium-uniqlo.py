import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

url = 'https://www.uniqlo.com/tw/zh_TW/'
driver.get(url)
driver.maximize_window()

search = driver.find_element(By.CLASS_NAME,'li-search')
search.click()

time.sleep(3)

# 捲動到特定位置
q = driver.find_element(By.CSS_SELECTOR,'img[alt="刷台新Richart卡享3.3%"]')
driver.execute_script("arguments[0].scrollIntoView(true);", q)
time.sleep(10)

# men = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div[3]/div[2]/div[1]/span[2]')
# men.click()

# time.sleep(3)

newproduct = driver.find_element(By.CSS_SELECTOR, 'img[alt="新品上市"]')
newproduct.click()

# time.sleep(5)

# rank = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[1]/div/div/div[27]/div/span')
# rank = driver.find_element(By.XPATH,'//*[@id="hmall-container"]/div/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/div/div/div[26]/div/span')
# rank.click()

# t = driver.find_element(By.XPATH, '//*[@id="hmall-container"]/div/div[1]/div[3]/div[4]/div[1]/div/div/input')
# t = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="請輸入關鍵字"]')
# t.send_keys('外套',Keys.ENTER)
# time.sleep(10)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME,'h-product-group'))
)


pcount = 0
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)
    # loading-paging

    # try:
    #     WebDriverWait(driver, 10).until(
    #         EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-paging'))
    #     )
    # except Exception as e:
    #     print(e)

    products = driver.find_elements(By.CLASS_NAME, 'ec-font-sub-title')
    if pcount == len(products):
        break
    pcount = len(products)

print(pcount)
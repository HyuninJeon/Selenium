from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


path = 'C:\study\Selenium\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

dimension_login = "https://thedimension.arabiz.live/store/3cfdeeb9-b3eb-42a7-b0cd-23d7a5b9ae80?coupon=true"
driver.get(dimension_login)
print('디멘션 로그인 페이지에 접속 하였습니다.')

time.sleep(5)

dimen_id = 'heidi.jeon@freedgrouptech.com'
dimen_pw = 'a5bb0a35e8b6469ca1b707087fa47895'

action = ActionChains(driver)

driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div/div[1]/header/div/img').click()

driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div/div[1]/nav/div[1]/div/section/div[1]/button').click()

driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div/div[1]/nav/div[1]/div/div/div').click()

(
action.send_keys(Keys.TAB).send_keys(dimen_id)
.send_keys(Keys.TAB).send_keys(dimen_pw).send_keys(Keys.TAB)
.send_keys(Keys.ENTER)
.perform()
)

print('로그인에 성공하였습니다.')

time.sleep(2) #페이지가 너무 빨리 넘어가서 에러남 -> time.sleep으로 해결!

#아메리카노 주문
driver.find_element(By.XPATH, '//*[@id="category-0"]/div[2]/div[1]/div/div').click()
time.sleep(2) #페이지가 너무 빨리 넘어가서 에러남 -> time.sleep으로 해결!
driver.find_element(By.XPATH, '//*[@id="option-select"]/section/div[2]/section/div[2]/p[1]').click()
driver.find_element(By.XPATH, '//*[@id="option-select"]/div[4]/button').click()

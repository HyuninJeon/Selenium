from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

path = 'C:\study\Selenium\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(3)

dimension_login = "https://thedimension.arabiz.live/store/3cfdeeb9-b3eb-42a7-b0cd-23d7a5b9ae80?coupon=true"
driver.get(dimension_login)
print('디멘션 로그인 페이지에 접속 하였습니다.')

time.sleep(5)

dimen_id = 'heidi.jeon@freedgrouptech.com'
dimen_pw = 'a5bb0a35e8b6469ca1b707087fa47895'
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div/div[1]/header/div/img').click()

driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div/div[1]/nav/div[1]/div/section/div[1]/button').click()

driver.find_element(By.ID, 'input-52').send_keys(dimen_id)

driver.find_element(By.ID, 'input-54').send_keys(dimen_pw)
driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div/div/div/div[1]/nav/div[1]/div/div/div/section/div/div[2]/button').click()

print('로그인에 성공하였습니다.')

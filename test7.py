from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd  
import time 

path = 'C:\study\Selenium\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(3)

dimension_login = "https://thedimension.arabiz.live/store/3cfdeeb9-b3eb-42a7-b0cd-23d7a5b9ae80"
driver.get(dimension_login)
print('디멘션 로그인 페이지에 접속 하였습니다.')

time.sleep(5)

dimen_id = 'heidi.jeon@freedgrouptech.com'
dimen_pw = 'a5bb0a35e8b6469ca1b707087fa47895'

driver.find_element('class', 'open-modal-button absolute left-2 top-2').click()
driver.find_element('class','sidebar-signup-login border-solid border border-yellow text-center text-1.5xs text-yellow py-1 px-4').click()

driver.find_element('id', 'input-60').send_keys(dimen_id)

driver.find_element('id', 'input-62').send_keys(dimen_pw)
driver.find_element('id', 'input-62').send_keys(Keys.ENTER)

print('로그인에 성공하였습니다.')

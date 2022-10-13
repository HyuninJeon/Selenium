from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd  
import time 
import pyperclip

path = 'C:\study\Selenium\chromedriver.exe'

driver = webdriver.Chrome(path) 
driver.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

user_id = "pingoo1121"
user_pw = 'konglove1121'

driver.get(url_login)
print('로그인 페이지에 접속 하였습니다.')

#이렇게 하면 네이버가 봇으로 인지해서 막음 driver.find_element('id', 'id').send_keys(user_id)
#driver.find_element('id', 'pw').send_keys(user_pw)
#driver.find_element('id', 'pw').send_keys(Keys.ENTER)

#복사 붙여넣기 이용
elem_id = driver.find_element('id', 'id')
elem_id.click()
pyperclip.copy(user_id) #복사붙여넣기 라이브러리
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

elem_id = driver.find_element('id', 'pw')
elem_id.click()
pyperclip.copy(user_pw)
elem_id.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

driver.find_element('id', 'log.login').click()
time.sleep(1)

print('로그인에 성공하였습니다.')

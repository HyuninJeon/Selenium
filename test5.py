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

driver = webdriver.Chrome(path) 
driver.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

user_id = "pingoo1121"
user_pw = "konglove1121"

driver.get(url_login)
print('로그인 페이지에 접속 하였습니다.')

driver.find_element('id', 'id').send_keys(user_id)

driver.find_element('id', 'pw').send_keys(user_pw)

driver.find_element('id', 'pw').send_keys(Keys.ENTER)

#driver.find_element('id', 'log.login').submit()

print('로그인에 성공하였습니다.')
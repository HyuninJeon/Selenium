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

url_login = "https://eclass.hufs.ac.kr/ilos/main/member/login_form.acl"

user_id = "201903141"
user_pw = "konglove12!"

driver.get(url_login)
print('로그인 페이지에 접속 하였습니다.')

time.sleep(5)

driver.find_element('id', 'usr_id').send_keys(user_id)

driver.find_element('id', 'usr_pwd').send_keys(user_pw)
driver.find_element('id', 'usr_pwd').send_keys(Keys.ENTER)

print('로그인에 성공하였습니다.')
from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd  
from selenium.webdriver.common.by import By


path = 'C:\study\Selenium\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#1. 검색할 키워드 입력
input = input('검색할 키워드를 입력하세요: ')

#크롬 드라이버로 원하는 url 접속
url = 'https://www.naver.com'
driver.get(url)
time.sleep(3)

#검색창에 키워드 입력 후 엔터
search = driver.find_element("id", 'query')
search.send_keys(input)
search.send_keys(Keys.RETURN)
time.sleep(2)

driver.find_element(Keys.ENTER)
time.sleep(2)

#뉴스탭 클릭
#driver.find_element("class", ' selected').click()
#driver.find_element('xpath' '//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[10]/a').click()
dfds



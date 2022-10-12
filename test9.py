from re import search
from urllib import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time
import pandas as pd  
from selenium.webdriver.common.by import By


path = 'C:\study\Selenium\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#크롬 드라이버로 원하는 url 접속
query = input('검색할 키워드를 입력해주세요: ')
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+query
time.sleep(2)

soup = bs(url, 'lxml')
news = soup.find('class', 'news_tit')

print(news.get_text())

titles = soup.select('a.news_tit')

for i in titles:
  title = i.get_text
  print(title)

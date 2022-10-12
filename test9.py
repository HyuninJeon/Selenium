from re import search
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

#1. 검색할 키워드 입력
input = input('검색할 키워드를 입력하세요: ')

#크롬 드라이버로 원하는 url 접속
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'query'
query = input('검색할 키워드를 입력하세요: ')


response = driver.get(url)
html_text = response.text
time.sleep(2)

soup = bs(html_text, 'html_parser')

print(soup.select_one('a.news_tit').get_text())

titles = soup.select('a.news_tit')

for i in titles:
  title = i.get_text
  print(title)

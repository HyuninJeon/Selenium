from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd  
import time 

finish_line = 10000

path = 'C:\study\Selenium\chromedriver.exe'

browser = webdriver.Chrome(path) 
browser.maximize_window()

browser.get("https://www.youtube.com")
time.sleep(2)
#사이트 방문

search = browser.find_element("name", "search_query")
time.sleep(2)
search.send_keys("뉴진스")
search.send_keys(Keys.ENTER)
time.sleep(2)
#키워드 검색

finish_line = 10000
# 원하는 위치 스크롤 내리기  
# finish_line = 40000 기준: 162 개
last_page_height = browser.execute_script("return document.documentElement.scrollHeight")

while True:
    # 우선 스크롤 내리기
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2.0)       # 작업 중간에 1이상으로 간격을 줘야 데이터 취득가능(스크롤을 내릴 때의 데이터 로딩 시간 때문)
    # 현재 위치 담기
    new_page_height = browser.execute_script("return document.documentElement.scrollHeight")
    
    # 과거의 길이와 현재 위치 비교하기
    if new_page_height > finish_line:
        break
    else: 
        last_page_height = new_page_height

html_source = browser.page_source
soup = BeautifulSoup(html_source, 'lxml')

# 첫 번째 컨텐츠의 제목, 채널명, url 정보 가져오기
# 첫 번째 컨텐츠 관련 부분 html 구조 떼어내기
# find: 해당 정보의 첫 번째 요소만 가져오기
test = soup.find("ytd-video-renderer", attrs={"class":'style-scope ytd-item-section-renderer'})

# 필요한 정보 가져오기
title = test.find("yt-formatted-string", attrs={"class":'style-scope ytd-video-renderer'}).get_text()
name = test.find("a", attrs={"class":'yt-simple-endpoint style-scope yt-formatted-string'}).get_text()
content_url = test.find("a", attrs={"class":'yt-simple-endpoint style-scope ytd-video-renderer'})["href"]

print(title, name, content_url)

# finish line까지 모든 검색 결과 정보 가져오기
# 모든 컨텐츠 관련 부분을 떼어내기
# find_all: 해당 정보의 모든 부분 가져오기
elem = soup.find_all("ytd-video-renderer", attrs={"class":'style-scope ytd-item-section-renderer'})

# 필요한 정보 가져오기
df = []
for t in elem:
    title = t.find("yt-formatted-string", attrs={"class":'style-scope ytd-video-renderer'}).get_text()
    name = t.find("a", attrs={"class":'yt-simple-endpoint style-scope yt-formatted-string'}).get_text()
    content_url = t.find("a", attrs={"class":'yt-simple-endpoint style-scope ytd-video-renderer'})["href"]
    df.append([name, title , 'https://www.youtube.com/'+content_url])
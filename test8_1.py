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
search = driver.find_element(By.XPATH, '//*[@id="query"]')
search.send_keys(input)
search.send_keys(Keys.RETURN)
time.sleep(2)

#뉴스탭 클릭
#driver.find_element("class", ' selected').click()
#driver.find_element('xpath' '//*[@id="lnb"]/div[1]/div/ul/li[2]/a').click()
news = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[10]/a')
driver.execute_script("arguments[0].click();", news)

news_titles = driver.find_elements(By.CSS_SELECTOR, '.news_tit')

for i in news_titles:
  title = i.text
  print(title)

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'lxml')

#find 함수: 조건에 해당하는 첫 번째 요소만 가져오기
elem = soup.find_all("news_tit", attrs={"class":'news_tit'})

df = []
for t in elem:
  content_url = t.find("news_tit", attrs={"class":'news_tit'}).get_text()
  title = t.find("a", attrs={"class":'news_tit'})["href"]
  df.append([title, 'https://www.naver.com/'+content_url])

## 자료 저장
# 데이터 프레임 만들기
new = pd.DataFrame(columns=['title', 'url_link'])

# 자료 집어넣기
for i in range(len(df)):
    new.loc[i] = df[i]

# 저장하기
# 현재 작업폴더 안의 data 폴더에 저장
df_dir = "./data/" # 저장할 디렉토리
new.to_csv(df_dir+"news_search_df.csv", index=False, encoding='utf8')

## 컬럼 정보 저장
# 컬럼 설명 테이블
col_names = ['title' ,'url_link']
col_exp = ['컨텐츠 제목', '연결 링크']

new_exp = pd.DataFrame({'col_names':col_names,
                        'col_explanation':col_exp})

# 현재 작업폴더 안의 data 폴더에 저장
df_dir = "./data/" # 저장할 디렉토리
new_exp.to_csv(df_dir+"news_col_exp.csv", index=False, encoding='utf8')

# 브라우저 닫기
driver.close()
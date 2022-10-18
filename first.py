from re import search
from selenium import webdriver #브라우저에 접근 가능
from selenium.webdriver.common.keys import Keys #Keys 클래스 == Shift 등을 포함한 키보드 입력
import time #n초 쉬게 해줌

driver = webdriver.Chrome(executable_path="chromedriver.exe")
url = "https://www.naver.com"
driver.get(url) #사이트방문

time.sleep(5) #5초

search = driver.find_element("id", 'query')
search.send_keys('오늘 날씨')
search.send_keys(Keys.ENTER)
time.sleep(2)
print(driver.current_url)
driver.close() #탭종료
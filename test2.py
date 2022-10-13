from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time 

path = 'C:\study\Selenium\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(3)

url = "https://www.naver.com"
driver.get(url) #사이트방문

driver.fullscreen_window() #전체화면 f12
time.sleep(1)
driver.maximize_window() #꽉차 화면
time.sleep(1)
driver.set_window_rect(101, 101, 598, 598)
#특정 좌표(x,y)와 크기(w,h)로 변경
time.sleep(1)

#현재 브라우저 창 크기 확인
print(driver.get_window_size())
print(driver.get_window_position())
print(driver.get_window_rect())

time.sleep(3) #3초 후 종료
driver.set_window_position(0,0)
driver.quit()
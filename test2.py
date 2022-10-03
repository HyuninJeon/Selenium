from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time 

driver = webdriver.Chrome(executable_path="chromedriver.exe")
url = "https://www.naver.com"
driver.get(url) #사이트방문

driver.fullscreen_window()
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.set_window_rect(100, 100, 600, 600)
#특정 좌표(x,y)와 크기(w,h)로 변경
time.sleep(1)

print(driver.get_window_position)

time.sleep(3) #3초 후 종료
driver.set_window_position(0,0)
driver.close()
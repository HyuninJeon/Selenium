from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time 

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.naver.com")
driver.get("https://www.youtube.com")
driver.get("https://www.google.com") #사이트방문

driver.back()
driver.back() #이전 창으로 2번 이동

driver.forward()
driver.forward()

time.sleep(3)
driver.quit() #웹브라우저 종료
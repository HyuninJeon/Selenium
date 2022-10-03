from re import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

driver.get("https://www.naver.com") 
driver.get("https://www.youtube.com")
#사이트방문

search = driver.find_element("name", "search_query")
time.sleep(2)
search.send_keys("뉴진스")
search.send_keys(Keys.ENTER)
time.sleep(2)

posts = driver.find_elements("id", "img")
posts[0].click()
time.sleep(2)

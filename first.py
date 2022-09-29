from selenium import webdriver as wd
driver = wd.Chrome(executable_path="chromedriver.exe")
url = "https://www.letskorail.com/ebizprd/prdMain.do"
driver.get(url) #사이트방문

tabs = driver.window_handles
print(tabs) #켜진 팝업창 갯수


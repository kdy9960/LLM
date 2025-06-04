from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
search = driver.find_element('name', 'q') # 요소를 찾는것으로 이것은 구글페이지에서 name이라는 요소가 q라고 명칭되어 있는 부분을 찾는다라는 의미
search.send_keys('날씨')
search.send_keys(Keys.RETURN)

time.sleep(10)
# 평가 1 - 네이버 키워드 검색하기
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

path='C:\\web_driver\\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get('https://www.naver.com')
time.sleep(1)

txt_query=input('크롤링할 키워드는 무엇입니까? ')

element=driver.find_element(By.ID,'query')
element.send_keys(txt_query)
time.sleep(1)
driver.find_element(By.ID,'search_btn').click()
time.sleep(1)
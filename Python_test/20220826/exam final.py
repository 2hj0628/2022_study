# 실습 보너스 - 다음 사이트 메뉴 분석하기

import urllib.request
import bs4

web_page=urllib.request.urlopen('https://www.daum.net')
result=bs4.BeautifulSoup(web_page,'html.parser')
menu=result.find('ul',class_='list_mainsvc')
for i in menu.find_all('li'):
    print(i.get_text(strip='True'))
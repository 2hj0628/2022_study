import urllib.request
import bs4

web_page=urllib.request.urlopen('https://www.naver.com')
result=bs4.BeautifulSoup(web_page, 'html.parser')
menu=result.find('ul',class_='list_nav')
for i in menu. find_all('li'):
    print(i.get_text(strip='True'))
# print(menu)
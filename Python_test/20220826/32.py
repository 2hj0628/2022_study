import urllib.request

web_page=urllib.request.urlopen('https://www.naver.com')

print(web_page.read())
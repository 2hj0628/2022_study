from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys
import math
import os
import pandas as pd
import xlwt

while True:
# 데이터 검색
    txt_query=input('(종료 0)크롤링할 키워드는 무엇입니까? ')
    if txt_query=='0':
        print('프로그램을 종료합니다.')
        break

    path='C:/web_driver/chromedriver.exe'
    driver=webdriver.Chrome(path)
    driver.get('https://korean.visitkorea.or.kr')
    time.sleep(1)

    element=driver.find_element(By.ID,'inp_search')
    element.send_keys(txt_query)
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'검색').click()
    time.sleep(1)

    print('대한민국 구석구석 프로그램을 실행합니다.')

# 데이터 출력
    try:
        cnt=int(input('(종료 0)크롤링할 건수를 입력하세요.(1~100) : '))
        if cnt<0 or cnt>100:
            raise
    except:
        print('다시 입력하세요.')
    else:
        if cnt==0:
            print('프로그램을 종료합니다.')
            break

    print(str(cnt)+'건의 데이터를 출력합니다.')
    start_time=time.time()

    no=1
    no2=[]
    title2=[]
    tag2=[]
    cnt_page=math.ceil(int(cnt)/10)
    
    for j in range(1,cnt_page+1):
        full_html=driver.page_source
        soup=BeautifulSoup(full_html,'html.parser')
        content_list = soup.find('ul','list_thumType type1')
        
        # 제목/태그 추출하기
        for i in content_list:
            try:
                title=i.find('div','tit').get_text()
            except AttributeError:
                continue
            else:
                no2.append(no)
                print('번호',no)
                title2.append(title)
                print('제목 :',title.strip())

            # 해쉬태그 추출하기
            tag=i.find('p','tag_type').get_text()
            tag2.append(tag)
            print('태그 :',tag.strip())
            print()
                
            if no==int(cnt):
                break
            no+=1
                
        # 페이지 넘기기 
        time.sleep(1)
        j+=1
        if j%5==1:
                driver.find_element(By.LINK_TEXT,'다음').click()
        else:
            if j==cnt_page+1:
                break
            else:
                driver.find_element(By.LINK_TEXT,str(j)).click()
    
# 데이터 저장
    while True:
        save=input('추출한 데이터를 저장하시겠습니까? (y / n) : ')
        if save=='y' or save=='Y' or save=='n' or save=='N':
            break
        else:
            print('y 혹은 n 을 입력해주세요.')
    if save=='n' or save=='N':
            print('프로그램을 다시 시작합니다.')
            continue
    
    while True:
        f_dir=input('파일을 저장할 폴더를 입력하세요. : ')

        if f_dir=='':
            f_dir='c:\\crawling\\'

        if not(os.path.isdir(f_dir)) :
            os.makedirs(f_dir)
            os.chdir(f_dir)
            print("입력하신 경로가 존재하지 않아 %s 폴더에 생성했습니다." %f_dir)
        else :
            os.chdir(f_dir)
            print("%s 폴더에 생성했습니다." %f_dir)

        while True:
            f_ext=input('저장할 파일의 종류를 입력하세요.(csv, xlsx, txt) : ')
            f_ext=('.'+f_ext)
            if f_ext=='.csv' or f_ext=='.xlsx' or f_ext=='.txt':
                break
            else:
                print('다시 입력하세요.')

        f_name=input('파일의 이름을 입력하세요. : ')

        if f_name=='':
            f_name='가을여행'

        file_name=f_dir+f_name+f_ext

        i=1
        while os.path.exists(file_name):
            file_name='%s%s(%d)%s' %(f_dir,f_name,i,f_ext)
            i+=1

        while True:
            check=input(file_name+'이 틀림없습니까? (y / n) : ')
            if check=='y' or save=='Y' or save=='n' or save=='N':
                break
            else:
                print('y 혹은 n 을 입력해주세요.')
        if check=='n' or check=='N':
            print('파일 저장을 다시 시작합니다.')
            continue
        if check=='y' or check=='Y':
            break

    korea_trip=pd.DataFrame()
    korea_trip['번호']=no2
    korea_trip['제목']=title2
    korea_trip['태그']=tag2

    if f_ext=='.csv':
        korea_trip.to_csv(file_name,encoding='utf-8-sig',index=False)
    if f_ext=='.xlsx':
        korea_trip.to_excel(file_name)
    if f_ext=='.txt':
        origin_stdout=sys.stdout
        f=open(file_name,'a',encoding='UTF-8')
        sys.stdout=f
        time.sleep(1)

        for i in range(no):
            print('번호',no2[i])
            print(title2[i])
            print(tag2[i])
            print()

        sys.stdout=origin_stdout
        time.sleep(1)
        f.close()
        
    print('파일 저장 경로 : %s' %file_name)

    end_time=time.time()
    result_time=end_time-start_time
    print('데이터 수집이 완료되었습니다.')
    print('데이터 수집부터 종료까지 걸린 소요시간은 총',str(round(result_time))+'초 입니다.')
    driver.quit()
    break
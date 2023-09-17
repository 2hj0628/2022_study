# 실습 12 - 자릿수 판별하기

try:
    num=int(input('숫자를 입력하세요 : '))
    if num<0:
        raise
except ValueError:
    print('다시 입력하세요.')
except:
    print('양의 정수를 입력하세요')
else:
    if len(num)==1:
        print('한 자릿수')
    if len(num)==2:
        print('두 자릿수')
    if len(num)==3:
        print('세 자릿수')
    if len(num)>3:
        print('세 자릿수이상')
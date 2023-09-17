# 실습 12 - 자릿수 판별하기

num=input('숫자를 입력하세요 : ')
check_num=bool(num)

# case 1
if check_num:
    if len(num)==1:
        print('한 자릿수')
    if len(num)==2:
        print('두 자릿수')
    if len(num)==3:
        print('세 자릿수')
    if len(num)>3:
        print('세 자릿수이상')
else:
    print('값을 입력하시오.')

# case 2
if check_num:
    if int(num)>=0:
        print('한 자릿수')
    if int(num)>=10:
        print('두 자릿수')
    if int(num)>=100:
        print('세 자릿수')
    if int(num)>=1000:
        print('세 자릿수이상')
else:
    print('값을 입력하시오.')


# 풀이

# case 1
num=input('숫자를 입력하세요 : ')

if not(num):
    print('값을 입력하지 않았습니다.')
else:
    if int(num)<0:
        print('양의 정수를 입력하여 주세요.')
    else:
        if int(num)>=1000:
            print('세 자릿수이상')
        elif int(num)>=100:
            print('세 자릿수')
        elif int(num)>=10:
            print('두 자릿수')
        elif int(num)>=0:
            print('한 자릿수')

# case 2
num=input('숫자를 입력하세요 : ')

if not(num):
    print('값을 입력하지 않았습니다.')
else:
    if int(num)<0:
        print('양의 정수를 입력하여 주세요.')
    else:
        if len(num)>=4:
            print('세 자릿수이상')
        elif len(num)>=3:
            print('세 자릿수')
        elif len(num)>=2:
            print('두 자릿수')
        elif len(num)>=1:
            print('한 자릿수')
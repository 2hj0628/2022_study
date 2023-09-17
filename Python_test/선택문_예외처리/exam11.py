# 실습 11 - 홀수 짝수 구분하기

try:
    num=int(input('양의 정수를 입력하세요 : '))
    if num<0:
        raise
except ValueError:
    print('다시 입력하세요.')
except:
    print('양의 정수를 입력하세요')
else:
    if float(num)%2==1:
        print('홀수입니다.')
    if float(num)%2==0:
        print('짝수입니다.')
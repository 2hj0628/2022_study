# 실습 6 - 피타고라스 정리
# 처리조건 : 빗변의 길이를 소수점 4번째 자리까지만 표현

import math

leng1=float(input('첫번째 직각변의 길이(cm) :'))
leng2=float(input('두번째 직각변의 길이(cm) :'))
result=leng1**2+leng2**2
print('빗변의 길이는',round(math.sqrt(result),4),'cm입니다.')

# 풀이
num1=float(input('첫번째 직각변의 길이(cm) :'))
num2=float(input('두번째 직각변의 길이(cm) :'))
result=(num1**2+num2**2)**0.5
print('빗변의 길이는',round(result,4),'cm입니다.')
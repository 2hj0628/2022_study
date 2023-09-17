# 실습 7 - 주사위 프로그램

# 예외처리할 것 없음

import random

print('주사위 프로그램을 시작합니다.')
print(random.randrange(1,7))

while(True):
    dice=input('아무키나 누르면 주사위가 던져집니다. 종료를 원하시면 q를 입력해주세요.: ')
    if dice=='q':
        break
    print(random.randrange(1,7))
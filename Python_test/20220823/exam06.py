# 실습 6 - UP & DOWN 게임

import random
answer=random.randrange(1,101)

while(True):
    num=int(input('예상 숫자를 입력하세요 : '))
    if answer>num:
        print('UP')
    elif answer<num:
        print('DOWN')
    elif answer==num:
        print('정답')
        break


import random
answer=random.randrange(1,101)
print(answer)

# case 1
num=int(input('예상 숫자를 입력하세요 : '))

while answer!=num:
    if answer>num:
        print('UP')
    elif answer<num:
        print('DOWN')
    # else:
    #     print('정답')
    num=int(input('예상 숫자를 입력하세요 : '))
print('정답')

# case 
# while(True):
#     num=int(input('예상 숫자를 입력하세요 : '))
#     if answer>num:
#         print('UP')
#     elif answer<num:
#         print('DOWN')
#     else:
#         print('정답')
#         break

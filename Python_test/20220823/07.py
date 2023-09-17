# 조건문과 break 보조 제어문을 활용해 조건에서 반복문을 완전히 빠져나올 수 있음

num=10
while num>0:
    if num==6:
        print('---end---')
        break
    print(num)
    num-=1
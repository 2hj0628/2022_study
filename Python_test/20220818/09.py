# 중첩 조건문
# 들여쓰기를 조정해서 조건문 안에 또 다른 조건문 추가 가능

num1=1
num2=2

if num1==1:
    if num2==2:
        print(1)    #num1==1 이고 num2==2인 경우
    else:
        print(2)    #num1==1 이고 num2!=2인 경우
else:
    print(3)        #num1!=1인 경우
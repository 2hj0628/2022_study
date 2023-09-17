# 실습 13 - 피보나치 수열

a=0
b=1
c=0
for i in range(20):
    print(a,end=' ')
    c=a+b
    a=b
    b=c
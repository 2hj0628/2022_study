# 실습 3 - 피보나치 수열

i=0
j=1
while i<100 and j<100:
    i+=j
    print(i)
    if i+j>100:
        break
    j+=i
    print(j)


# 풀이
a=0
b=1
c=0         #임의로 0으로 둠

while c<100:
    c=a+b
    print(c)
    a=b
    b=c

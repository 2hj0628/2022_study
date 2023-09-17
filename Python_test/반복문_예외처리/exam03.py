# 실습 3 - 피보나치 수열

# 예외처리할 것 없음

i=0
j=1
while i<100 and j<100:
    i+=j
    print(i)
    if i+j>100:
        continue
    j+=i
    print(j)

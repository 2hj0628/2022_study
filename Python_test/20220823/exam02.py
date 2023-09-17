# 실습 2 - 특정 숫자 반복 출력하기

i=0
while i<30:
    i+=1
    print(i%4)

for i in range(30):
    i+=1
    print(i%4)


# 풀이

i=1
while i<31:
    print(i%4)
    i+=1

for i in range(1,31,1):
    print(i%4)
# 실습 1 - 홀수만 출력하기

# 1부터 100까지의 홀수만 출력하기

# case 1
for i in range(100):
    if i%2==1:
        print(i)

# case 2
i=1
while i<100:
    print(i)
    i+=2

# case 3
i=0
while i<100:
    i+=1
    if i%2==0:
        continue
    print(i)

# case 4
i=0
while i<100:
    i+=1
    if i%2==1:
        print(i)


# 풀이
i=1
while i<100:
    print(i)
    i+=2

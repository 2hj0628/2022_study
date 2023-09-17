# 실습 1 - 홀수만 출력하기
# 1부터 100까지의 홀수만 출력하기

# 예외처리할 것 없음

i=0
while i<100:
    i+=1
    if i%2==0:
        continue
    print(i)
    
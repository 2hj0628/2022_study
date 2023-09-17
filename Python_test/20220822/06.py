# 제어문을 여러개 사용할 경우, 들여쓰기 주의
# for - 큰 반복문 - 반복횟수 두번
#   for - 작은 반복문 - 반복횟수 세번
# 큰 반복문 한번 수행하고, 작은 반복문을 세번 수행한다 * 2

for i in range(2):      #0 012 -> 1 012
    print('i-',i)
    for j in range(3):
        print('j-',j)
print()

for i in [1,2,3]:       #1 10 1 20 ->2 10 2 20 ->3 10 3 20
    for j in (10,20):
        print(i)
        print(j)
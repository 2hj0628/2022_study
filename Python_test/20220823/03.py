# continue를 활용해 한차례 반복을 건너뛸 수 있음

str='hello'
cnt=0

for i in str:
    if i=='e':
        print('i is e')
        continue
    cnt+=1      #cnt+1을(continue 밑에꺼) 한번 건너뜀

print(cnt)
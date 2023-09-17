# 조건문과 continue 보조 제어문을 활용해 특별한 조건에 해당 반복을 건너뛸 수 있음

# num=1             
# while num<=10:
#     if num==6:
#         continue
#     print(num)
#     num+=1            #1 2 3 4 5 6부터 건너뜀(프린트x)

num=0
while num<10:
    num+=1
    if num==6:
        continue
    print(num)

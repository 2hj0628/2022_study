# 리스트 내포 - 조건문을 함께 사용할 수 있음
list1=[]
for i in range(5):
    if i%2==0:
        list1.append(i)
print(list1)

print([i for i in range(5) if i%2==0])
# 리스트 내포의 중첩

list1=[]
for i in range(3):
    for j in range(3):
        list1.append(i+j)
print(list1)

print([i+j for i in range(3) for j in range(3)])    #식 큰반 작반
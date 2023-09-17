# 요소 값을 아이템 변수로 할당하여 응용 가능

list1=[[1,2],[3,4],[5,6]]
for i in list1:
    print(i)

print(list1[0][0]+list1[0][1])
print(list1[1][0]+list1[1][1])
print(list1[2][0]+list1[2][1])
print()

sum=0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        if j==0:
            sum+=list1[i][0]
        if j==1:
            sum+=list1[i][1]
    print(sum)
    sum=0
print()

for i,j in list1:
    print(i+j)

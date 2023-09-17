# 반복 객체의 값을 바로 가져와서 사용하거나, range(), len()
# 함수를 활용해 인덱스로 접근 또한 가능하다

list1=['a',9,[1,2,3],('a','b')]
for i in list1:
    print(i)
print()

for i in range(len(list1)):
    print(list1[i])
print()


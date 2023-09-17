# append() 함수 : 해당 값을 요소로 추가

list1=[1,2,3]
list1.append(4)
print(list1)
print()
# list1.append(4,5,6)     #TypeError
list1.append([4,5,6])       #list를 추가
print(list1)
print(list1[4][1])
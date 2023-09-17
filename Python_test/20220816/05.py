# index() 함수 : 리스트에 해당 값이 있으면 해당 값의 인덱스를 반환(첫번째)

list1=[1,2,2,2,3,3,4,5,6,7,8,9]
print(list1)
print(list1.index(2))   
print(list1.index(5))
print(list1.index(9))
print()
list1.reverse()
print(list1)
print(list1.index(2))
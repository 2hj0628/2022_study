# 리스트의 여러 명령어들

list1=['A','B','C','D','E','E']
print(list1)

list1.append('F')
print(list1)

list1.insert(2,'b')     #2부터 뒤로 밀림
print(list1)

list1.extend(['G','H']) #끝에 들어옴
print(list1)

print(list1.count('C'))
print(list1.index('D'))
list1.remove('E')
print(list1)
print()

list2=[3,1,4,5,2]
print(list2)

list2.sort()
print(list2)

list2.reverse()
print(list2)

print(len(list2))
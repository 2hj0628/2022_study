# shallow copy(얕은 복사)
# 리스트와 같은 변형 객체에서는 다른 방법으로 복사를 해야
# B를 수정해도 A가 바뀌지 않게 된다.

# 문제점
# list_A=['ABC','DEF']
# list_B=list_A
# print(list_A)
# print(list_B)
# print()
# list_B.append('GHI')
# print(list_A)
# print(list_B)
# print(id(list_A))
# print(id(list_B))

list_A=['ABC','DEF']
list_B=list_A.copy()  #방법1
# list_B=list_A[:]        #방법2
print(list_A)
print(list_B)
print()
print(id(list_A))
print(id(list_B))
print()
list_B.append('GHI')
print(list_A)
print(list_B)
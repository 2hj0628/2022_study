# 추가 및 삭제 방법
# set의 함수

# 하나의 값을 추가하려면 add() 함수 활용
s1={1,2,3}
print(s1)
s1.add(4)
print(s1)

# 여러 값을 추가할 때는 update() 함수로 리스트에 값을 넣어 추가
# set에서 list는 추가할 때의 용도로만 사용
s1.update([5])
print(s1)

s1.update([6,7,1])
print(s1)

# 삭제는 remove()함수를 활용
# set, list 의 함수
s1.remove(5)
print(s1)

# test
li=[1,1,2,2,3,3]
print(li)
li.remove(1)    #왼쪽부터 처음 1 한개만 지워짐 
print(li)
del li[0]
print(li)
li.clear()
print(li)

del li          #값을 지우는게 아니라 아예 사라짐
print(li)
# 튜플의 인덱싱, 슬라이싱, 리스트로 만들기

num=(1,2,3,4,5)

# 인덱싱
print(num)
print(num[0])           #맨처음 요소
print(num[-1])          #맨끝 요소
print(num[len(num)-1])  #맨끝 요소
print(num[4])           #맨끝 요소
print()

# 슬라이싱
print(num[1:3])
print(num[1:3:1])
print(num[0:5:2])
print(num[::2])
print()

# 리스트
list1=list(num)
print(list1)
list1[0]=10
print(list1)
num=tuple(list1)
print(num)
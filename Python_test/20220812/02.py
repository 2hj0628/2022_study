# 문자열과 같이 인덱스와 슬라이싱 연산 가능

list1=[1,2,3,4,5,6,7,8,9]
print(list1[0])
print()

print(list1[5])
print()

print(list1[8])
print()

# 인덱스는 0부터 시작하기 때문에 리스트 길이를 구한 후 -1을 함
print(list1[len(list1)-1])
print()

# 인덱스에 -1을 주었을 경우 리스트의 맨 마지막 요소를 가리킴
print(list1[-1])
print()

# 슬라이싱
print(list1[0:4])
print()
print(list1[0:4:1])

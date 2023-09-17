# 사전(dict) 정리

# key를 이용하여 value 추출하기

dict1={1:'사과',2:'banana','three':3,'four':4}
print(dict1)
print(dict1[2])
print(dict1['three'])
print()

# dict에 key와 value 추가하기
dict1['second']=2   #존재하지 않는 key라 추가됨
print(dict1)

# key가 존재한다면 value가 변경
dict1[2]='two'
print(dict1)

# key가 존재한다면 항목 삭제
del dict1['second']
print(dict1)
print()

# key 존재 여부 확인하기
print(3 in dict1.keys())

# value 존재 여부 확인하기
print(3 in dict1.values())
print()

# value를 추출한 후 삭제
print(dict1.pop('three'))
print(dict1)

# dict 초기화
dict1.clear()
print(dict1)
# 리스트의 요소 수정 및 변경

list1=['A','B','C']

print(list1)
list1[1]='b'    #값을 하나만 바꿀때
print(list1)
list1[1:2]=['B','b','bear'] #1이상 2미만(사이)에 넣기
# list1[1]=['B','b','bear'] #결과 다름
print(list1)

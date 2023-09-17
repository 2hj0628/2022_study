# sort() 함수 : 오름차순(순방향)으로 값 정렬(정렬 방식 변경 가능)

list_num=[100,20,-10,99,72,5,10,9,-1]

print(list_num)
print()

# 숫자 리스트 오름차순 정렬
list_num.sort(reverse=False) #reverse=False 생략가능(기본값)
print(list_num)

# 숫자 리스트 내림차순 정렬
list_num.sort(reverse=True)
print(list_num)

# 문자열 리스트
list_str1=['w','h','i','t','e','m','a','s','k']
list_str2=['B','l','a','c','K','M','a','s','k']

# 문자열 리스트 정렬(소문자만)
list_str1.sort()
print(list_str1)

# 문자열 리스트 정렬(대문자/소문자)
list_str2.sort()
print(list_str2)
print()
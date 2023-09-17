# find() : 해당 문자열의 인덱스를 반환(없는 경우 -1 반환)

str1='abcdef'
print(str1.find('e'))
print(str1.find('g'))

# 그외 문자열 함수 확인
print(dir(str))
print(len(dir(str)))

str2=list(str1)
print(str2)

#['hello','happy','coding']
[['h','e','l','l','o'],...,... ]
str1='hello happy coding'
str2=str1.split(' ')
print(str2)
str3=list(str2[0])
print(str3)
list1=list()

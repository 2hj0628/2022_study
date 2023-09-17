# 참고
# 1 더하기 2는 3입니다.

str1='{} 더하기 {}는 {}입니다.'.format(1,2,1+2)
print(str1)

str2='{n1} 더하기 {n2}는 {n3}입니다.'.format(n1=1,n2=2,n3=1+2)
print(str2)

# 풀이
str3='{} 더하기 {}는 {}입니다.'.format(1,2,3)
print(str3)
str4='{0} 더하기 {1}는 {2}입니다.'.format(1,2,3)
print(str4)
str5='{zero} 더하기 {one}는 {two}입니다.'.format(zero=1,one=2,two=3)
print(str5)

list1=[1,2,3]
str6='{} 더하기 {}는 {}입니다.'.format(list1[0],list1[1],list1[2])
print(str6)
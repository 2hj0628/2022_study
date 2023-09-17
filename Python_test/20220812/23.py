# 교집합, 합집합, 차집합의 연산도 지원

s1=set([1,2,3,4,5])
s2=set([4,5,6,7,8,9,9])

print(s1,type(s1))
print(s2,type(s2))

# 교집합
print(s1.intersection(s2))
print(s1&s2)

# 합집합
print(s1.union(s2))
print(s1|s2)

# 차집합
print(s1.difference(s2))
print(s1-s2)
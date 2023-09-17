# 리스트와의 차이점 : 값의 변경이 불가능

l=[1,2,3]
t=(1,2,3)

print(l,type(l))
print(t,type(t))
print()

l[0]=9
print(l)
print()

# t[0]=9      TypeError
# print(t)
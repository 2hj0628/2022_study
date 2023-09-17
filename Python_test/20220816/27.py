# copy() 함수 : 사전의 복사
# 새로운 객체를 만들어서 복사

dict1={'a':1,'b':2,'c':3}
print(dict1,id(dict1))

dict2=dict1.copy()
print(dict2,id(dict2))

dict3=dict1
print(dict3,id(dict3))
print()

dict1['a']=2
dict2['b']=3
print(dict1)
print(dict2)
print(dict3)

# update() 함수 : 두 사전의 병합
# a.update(b) ; a 사전에 b 사전을 새롭게 업데이트 하는 함수로 a 값만 변경됨

dict1={'a':1,'b':2,'c':3}
dict2={'c':2,'d':4,'e':5}

print(dict1,type(dict1))
print(dict2,type(dict2))
print()

dict1.update(dict2)
print(dict1)
print(dict2)
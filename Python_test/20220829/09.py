# 인스턴스 또한 별도의 이름 공간을 할당

a=0

class S1:
    a=1

print('S1 :',S1.a)

x=S1()
print('x.a :',x.a)
print('-------')

x.a=10
print('a :',a)
print('x.a :',x.a)
print('S1.a :',S1.a)
# 클래스는 별도의 이름 공간이 할당

class SimpleClass:
    pass

c1=SimpleClass()
c2=SimpleClass()

c1.a=10
print(c1.a)
print(c2.a)
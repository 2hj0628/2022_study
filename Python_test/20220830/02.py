# 다형성
class Animal:
    def cry(self):
        return '엉엉'

class Dog(Animal):
    def cry(self,a,b):
        return a*b
class Duck(Animal):
    def cry(self,a,b):
        return a+b
class Fish(Animal):
    pass

a=Dog()
# print(a.cry())      #매개변수 없어서 에러(오버로딩)
print(a.cry('멍멍',3))
b=Duck()
print(b.cry(3,4))
c=Fish()
print(c.cry())      #pass했어도 부모의 엉엉
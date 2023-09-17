# isinstance(인스턴스,클래스)

class A:
    def __init__(self,i):
        self.i=i
    def __add__(self,other):
        return A(self.i+other)

i=A(10)
i=i+1
print(i)    #인스턴스가 출력
print(type(i))  #클래스 A가 출력
print(isinstance(i,A))  #i가 A의 인스턴스인가?
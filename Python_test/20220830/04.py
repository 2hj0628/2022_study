# 상속관계 파악하기

class A:
    pass

class B:
    def f(self):
        pass

class C(B):
    pass

a=A()
print(isinstance(a,A))
print(isinstance(a,B))
print(isinstance(a,C))
print()

print(issubclass(A,B))
print(issubclass(B,C))  #부모라서 안됨
print(issubclass(C,B))
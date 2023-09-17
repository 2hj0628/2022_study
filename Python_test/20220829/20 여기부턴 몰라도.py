# 연산자 오버로딩

# a=1
# b=2
# print(a+b)

class A:
    def __init__(self,i):
        self.i=i

n=A(40)
# print(n+1)    #에러발생-인스턴스간 연산이 되지 않음
print(n.i+1)
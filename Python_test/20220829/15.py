# 클래스 멤버
class Var:
    #클래스 변수
    c_mem=100
    
    def f(self):
        #인스턴스 변수
        self.i_mem=200

v1=Var()
v2=Var()
print(Var.c_mem)
print(v1.c_mem)
print(v2.c_mem)
print()

v1.c_mem=50
print(Var.c_mem)
print(v1.c_mem)
print(v2.c_mem)
print()

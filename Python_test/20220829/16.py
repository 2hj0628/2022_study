# 인스턴스 멤버
class Var:
    #클래스 변수
    c_mem=100
    
    def f(self):
        #인스턴스 변수
        self.i_mem=200

# 인스턴스 생성
v1=Var()
v2=Var()
# 인스턴스 메소드 호출
v1.f()
# 인스턴스 변수 사용 가능
print(v1.i_mem)
# print(v2.i_mem)   #오류발생
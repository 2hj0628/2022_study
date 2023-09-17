# 인스턴스 메소드

class C:
    def ham(self,x,y):
        print('instance method',x,y)
    
c=C()
c.ham(1,2)

# 인스턴스 객체없이 클래스에서 직접 호출
# C.ham(1,2)    #오류발생
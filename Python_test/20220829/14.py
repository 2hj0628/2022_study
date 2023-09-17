# 정적 메소드

class D:
    @staticmethod       #데코레이터 필요
    def spam(x,y):
        print('static method',x,y)

# 인스턴스 객체 없이 클래스에서 직접 호출
D.spam(1,2)             #클래스 이름으로 접근

d=D()
# 인스턴스 객체를 통해서도 호출 가능
d.spam(3,4)
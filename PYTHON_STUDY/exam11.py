import math

class Circle:

    # 생성자
    def __init__(self,radius):
        # self.radius=radius  바깥에서 접속 가능함(-10)
        self.__radius=radius

    # 둘레 구하는 메서드
    def get_round(self):
        return 2*math.pi*self.__radius
    
    # 넓이 구하는 메서드
    def get_area(self):
        return math.pi*(self.__radius**2)

    # getter setter 메서드
    def get_radius(self):
        return self.__radius  # 내부적(프라이빗)

    def set_radius(self,value):
        if value<=0:
            raise TypeError('반지름은 양의 숫자여야 합니다.')
        self.__radius=value


circle1=Circle(10)
# circle1.radius=-10
print('둘레 :',circle1.get_round())
print('넓이 :',circle1.get_area())
print()

print(circle1.get_radius())
print()

circle1.set_radius(5)
print('둘레 :',circle1.get_round())
print('넓이 :',circle1.get_area())
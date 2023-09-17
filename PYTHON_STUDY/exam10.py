import math

class Circle:

    # 생성자
    def __init__(self,radius):
        self.radius=radius

    # 둘레 구하는 메서드
    def get_round(self):
        return 2*math.pi*self.radius
    
    # 넓이 구하는 메서드
    def get_area(self):
        return math.pi*(self.radius**2)

circle1=Circle(10)
circle1.radius=-10
print('둘레 :',circle1.get_round())
print('넓이 :',circle1.get_area())
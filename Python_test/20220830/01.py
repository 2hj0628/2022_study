# 상속
class Person:
    def __init__(self,name,phone=None):
        self.name=name
        self.phone=phone
    def __str__(self):
        return '<Person{0}{1}>'.format(self.name,self.phone)

class Employee(Person):
    def __init__(self,name,phone,position,salary):
        Person.__init__(self,name,phone)
        self.position=position
        self.salary=salary
    def __str__(self):
        return '<Person{0}{1}{2}{3}>'.format(self.name,self.phone,self.position,self.salary)

p1=Person('라이언',1234)
print(p1.name)
print(p1.phone)
print(p1)
print()

m1=Employee('어피치',5678,'대리',200)
print(m1.name)
print(m1.phone)
print(m1.position)
print(m1.salary)
print(m1)
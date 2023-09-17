class Parent:
    
    def __init__(self):
        self.value = '부모의 값'
        print('Parent 클래스의 생성자 __init__ 메서드가 호출되었습니다.')
        
    def to_string_test(self):
        print('Parent 클래스의 to_string_test 메서드가 호출되었습니다.')
        


class Child(Parent):
    
    def __init__(self):
        Parent.__init__(self)
        print('Parent 클래스의 생성자 __init__ 메서드가 호출되었습니다.')


child = Child()
child.to_string_test()
print(child.value)

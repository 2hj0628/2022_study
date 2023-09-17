# 소멸자
class MyClass:
    def __init__(self):
        print('클래스가 생성되었습니다.')
    def __del__(self):
        print('클래스가 소멸되었습니다.')

# 인스턴스 생성
c=MyClass()
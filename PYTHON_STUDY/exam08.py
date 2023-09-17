class Test:

    def __init__(self,name):
        self.name=name
        print('{} - 생성'.format(self.name))

    def __del__(self):
        print('{} - 소멸'.format(self.name))

Test('A')
Test('B')
Test('C')
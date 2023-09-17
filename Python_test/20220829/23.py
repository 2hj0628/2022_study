# len() 내장 함수

class MyClass:
    def __init__(self,end):
        self.end=end
    def __len__(self):
        return self.end

s1=MyClass(10)
print(len(s1))

s2=20
# print(len(s2))    #오류발생
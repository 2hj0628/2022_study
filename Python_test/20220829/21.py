# 수치 연산자 오버로딩

class MyInteger:
    def __init__(self,i):
        self.i=i
    def __add__(self,other):
        return self.i+other
    def __radd__(self,other):
        return self.i+other
    def __sub__(self,other):
        return self.i-other
    def __rsub__(self,other):
        return other-self.i
    def __mul__(self,other):
        return self.i*other
    def __rmul__(self,other):
        return self.i*other
    def __truediv__(self,other):
        return self.i/other
    def __rtruediv__(self,other):
        return other/self.i
    
# i=MyInteger(10)
# print(i+10)
# print(10+i)       #위에 r 안붙히면 오류발생
# print(i-5)
# print(5-i)      #other-self.i로 바꿔줘야 -5
# print(i*2)
# print(2*i)
# print(i/3)
# print(3/i)

i=MyInteger(10)
i=i+10
print(i)
i+=5
print(i)
i-=5
print(i)
i/=5
print(i)
i*=3
print(i)
# 비교 연산자 오버로딩

class MyInteger:
    def __init__(self,i):
        self.i=i
    def __gt__(self,y):
        return self.i>y
    def __ge__(self,y):
        return self.i>=y
    def __lt__(self,y):
        return self.i<y
    def __le__(self,y):
        return self.i<=y
    def __eq__(self,y):
        return self.i==y
    def __ne__(self,y):
        return self.i!=y

c=MyInteger(10)
d=MyInteger(20)
print(c>1)
# print(1<c)      #비교연산자는 r을 안붙혀도 됨
print(c>=1)
# print(1<=c)     #self는 왠만하면 왼쪽에
print(c<1)
print(c<=1)
print(c==1)
print(c!=1)
print()

print(c>d)
print(c>=d)
print(c<d)
print(c<=d)
print(c==d)
print(c!=d)
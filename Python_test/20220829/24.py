# getitem() 내장 함수

class MyClass:
    def __init__(self, end):
        self.end=end
    def __getitem__(self,k):
        if k<0 or self.end<=k:
            raise IndexError('out of Index - '+str(k))
        return k*k

s1=MyClass(10)
# print(s1[-1])
print(s1[0])
print(s1[1])
print(s1[9])
# print(s1[10])
print()

print(list(s1))
print(tuple(s1))
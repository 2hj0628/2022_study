# self를 적어주지 않으면 외부에서 해당 메소드를 찾게 됨
def class_set(i):
    print('외부함수 입니다. - ',i)

class MyClass:
    # set 메소드
    def class_set(self,v):
        self.value=v
    # get 메소드
    def class_get(self):
        return self.value
    # 숫자를 1증가시키는 메소드
    def class_incr(self):
        class_set(self.value+1)    #self 없앰

c=MyClass()
print(c)
print(MyClass)
c.class_set(1)
print(c.class_get())
print()

c.class_incr()
print(c.class_get())
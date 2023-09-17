# 객체 내부의 메소드를 호출할 수 있음

class MyClass:
    # set 메소드
    def class_set(self,v):
        self.value=v
    # get 메소드
    def class_get(self):
        return self.value
    # 숫자를 1증가시키는 메소드
    def class_incr(self):
        self.class_set(self.value+1)    #내부 메소드 호출

c=MyClass()
c.class_set(1)
print(c.class_get())
print()
c.class_incr()
print(c.class_get())
c.class_incr()
print(c.class_get())
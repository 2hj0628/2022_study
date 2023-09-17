# 메소드의 정의

class MyClass:
    def class_set(self,v):      #return 없음
        self.value=v            #인스턴스 메소드
    def class_get(self):
        return self.value

# 메소드의 호출
# 인스턴스 객체를 활용해 메소드 호출
#self는 기본적으로 c를 지칭(value 값만 넣어주면 됨)
c=MyClass()
c.class_set('10')
print(c.class_get())

# 클래스 객체를 활용해 메소드 호출
c=MyClass()   #인스턴스 생성
MyClass.class_set(c,'10')
print(MyClass.class_get(c))
# 람다의 기본 매개변수
print((lambda a,b=1:a+b)(3))

# 람다의 키워드 매개변수
print((lambda a,b:a+b)(b=1,a=2))

# 람다의 가변 매개변수
print((lambda a,*b:a*b)(3,3,4,5))   #3,4,5를 3번 반복(문자열처럼)

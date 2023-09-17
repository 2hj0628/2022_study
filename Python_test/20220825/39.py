# 두개 이상의 값을 반환하면, 결과값은 튜플로 반환

def func(a,b):
    return a,b

result=func(1,2)
print(result)
print(type(result))

# 매개변수의 자료형은 동적으로 결정되며, 
# 호출되는 순간 해당 인자에 전달되는 객체에 따라 
# 자료형이 결정됨

result1=func('a',['리스트',1])
print(result1)
print(type(result1))
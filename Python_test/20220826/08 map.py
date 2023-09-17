# map 내장 함수

def func(x):
    return x*x

a=[1,2,3,4,5]
b=map(func,a)
print(type(b))
print(list(b))
# print(b)
# filter 내장 함수

def func(x):
    return x>2

a=[1,2,3,4,5]
print(type(filter(func,a)))
print(list(filter(func,a)))
# map 함수와 동일하게 구현하기

def func(x):
    return x*x

a=[1,2,3,4,5]
b=[]
for x in a:
    y=func(x)
    b.append(y)

print(b)
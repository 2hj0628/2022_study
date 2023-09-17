# filter 내장함수와 동일하게 구현하기

def func(x):
    return x>2

a=[1,2,3,4,5]
b=[]

for x in a:
    if func(x):     #==True:
        b.append(x)

print(b)

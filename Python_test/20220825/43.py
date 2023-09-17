# 전역변수

a=10
print(a)

def func():
    global a
    a=20
    print(a)

func()
print(a)
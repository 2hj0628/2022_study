# 조건문과 함께 사용 가능

# 가운데 조건이 참이면 왼쪽 거짓이면 오른쪽
# 1은 홀수이므로 3출력, 2(짝수)였으면 2
print((lambda a,b:a if a%2==0 else b)(1,3))

def func(a,b):
    return(a if a%2==0 else b)
print(func(1,3))

# 풀이
def func(a,b):
    if a%2==0:
        return a
    else:
        return b
print(func(1,3))
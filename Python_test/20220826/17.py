# 팩토리얼 계산

def factorial(n):
    if n==0:        #n==1도 상관없음
        return 1
    return n*factorial(n-1)

print(factorial(5))
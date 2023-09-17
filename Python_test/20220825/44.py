# 함수에서의 값 전달
# 밖에서 10이여도 20으로 덮어씀, 지역변수가 더 셈
# 변수가 바뀐건 아님

a=10
print(a)

def func(b):    
    b=20
    print(b)

func(a)
print(a)
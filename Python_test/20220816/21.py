# 함수의 리턴

# 리스트
def test1():
    return[1,2]

result1=test1()
print(result1,type(result1))

# 튜플
def test2():
    return(1,2)

result2=test2()
print(result2,type(result2))

# 참고 - 튜플
def test3():
    return 1,2

result3=test3()
print(result3,type(result3))

# 집합(set)
def test4():
    return{1,2}

result4=test4()
print(result4,type(result4))

# 사전(dict)
def test5():
    return{'a':1,'b':2}

result5=test5()
print(result5,type(result5))

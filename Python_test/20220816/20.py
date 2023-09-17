# 값의 할당 및 리턴

tuple1=1,2,3    #튜플 - 상수개념
print(tuple1,type(tuple1))
print()

x,y,z=1,2,3
print(x,y)

def test():
    return(1,2) #여러개의 값을 그룹화 시키는 용도

num1,num2=test()    #=1,2

print(num1,type(num1))
print(num2,type(num2))
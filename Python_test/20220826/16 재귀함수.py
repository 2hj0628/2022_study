# 종료 조건이 필요함

def recursive(num):
    print(num)
    num+=1
    if num==100:
        return
    recursive(num)

recursive(1)
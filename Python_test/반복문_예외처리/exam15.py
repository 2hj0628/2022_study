# 실습 15 - 숫자 건너뛰고 종료하기
# 음수, 실수, num1>num2

while True:
    try:
        num1=int(input('마지막 숫자는 : '))
        num2=int(input('뛰어넘을 숫자는 : '))
        if num1<1 or num2<1 or num1<num2:
            raise
    except:
        print('다시 입력하세요.')
    else:
        for i in range(num1+1):
            if i==num2:
                continue
            else:
                print(i)
                i+=1 
        break

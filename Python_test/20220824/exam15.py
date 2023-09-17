# 실습 15 - 숫자 건너뛰고 종료하기

# 음수, 실수, num1>num2

while True:
    num1=input('마지막 숫자는 : ')
    num2=input('뛰어넘을 숫자는 : ')
    if num1=='' or num2=='':
        print('값을 입력하세요.')
    elif '.' in num1 or '.' in num2:
        print('실수는 사용할 수 없습니다.')
    else:
        n_num1=int(num1)
        n_num2=int(num2)
        if n_num1<n_num2 or n_num1<1 or n_num2<1:
            print('다시 입력하세요.')
            continue
        i=0
        for i in range(n_num1+1):
            if i==n_num2:
                continue
            else:
                print(i)
                i+=1 
        break

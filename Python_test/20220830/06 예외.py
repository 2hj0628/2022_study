num=input('정수 입력 : ')

if num.isdigit():
    num=float(num)

    print('반지름 : ',num)
    print('둘레 : ',2*3.14*num)
    print('넓이 : ',3.14*num*num)
else:
    print('예외 처리 되었습니다.')
num=input('정수 입력 : ')

try:
    num=float(num)

    print('반지름 : ',num)
    print('둘레 : ',2*3.14*num)
    print('넓이 : ',3.14*num*num)
except:
    print('예외 발생')
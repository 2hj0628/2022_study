# 실습 9 - 가우스 계산기

num=0
while num!=1:
    try:
        num=int(input("(종료 '1')숫자 입력 : "))
        if num<1:
            raise
    except:
        print('다시 입력하세요.')
    else:
        result=((num+1)*(num/2))
        print(round(result))
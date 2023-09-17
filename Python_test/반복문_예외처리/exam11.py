# 실습 11 - 끼니 계산하기

meal=['아침','점심','저녁','야식']

num=1
while num!=0:
    try:
        num=int(input("(종료 '0')며칠이 지났습니까 : "))
        if num<0:
            raise
    except:
        print('다시 입력하세요.')
    else:
        for i in range(num):
            for j in meal:
                print(j)
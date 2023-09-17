# 실습 14 - 홀수 짝수 생성하기

# 1,2 아니면 다시 묻기
# 0은 종료

while True:
    try:
        num=int(input('홀수는 1, 짝수는 2를 입력해주세요 : '))
        if num!=0 and num!=1 and num!=2:
            raise
    except:
        print('다시 입력하세요.')
    else:
        if num==0:
            break
        for i in range(num,101,2):
            print(i,end=' ')
        print()
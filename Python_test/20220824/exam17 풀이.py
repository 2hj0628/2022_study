# 실습 17 - 배스킨라빈스 31

print('배스킨라빈스 31')

number=1
while number<31:
    # player1
    while True:
        p1=int(input('(0 입력시 종료) 플레이어 1 순서, 입력할 숫자는?'))

        if p1==0:
            break
        
        if p1<number or p1>number:
            print('잘못된 숫자를 입력했습니다. 다시 입력하세요.')
            continue

        number=p1+1

    # player1 - 출력
    for i in range(number,31+1):
        print(i,end=' ')
    print('')
    # player2
    while True:
        p2=int(input('(0 입력시 종료) 플레이어 2 순서, 입력할 숫자는?'))

        if p2==0:
            break

        if p2<number or p2>number:
            print('잘못된 숫자를 입력했습니다. 다시 입력하세요.')
            continue

        number=p2+1

    # player2 - 출력
    for i in range(number,31+1):
        print(i,end=' ')
    print('')
print('30까지 외쳤습니다. 게임이 끝났네요.')
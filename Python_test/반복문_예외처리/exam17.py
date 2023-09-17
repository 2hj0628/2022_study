# 실습 17 - 배스킨라빈스 31

# 잘못눌러도 턴 안바뀜

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]


print('배스킨라빈스 31')
while True:
    if list[0]==31:
        print(31)
        print('30까지 외쳤습니다. 게임이 끝났네요.')
        break
    try:
        p1=int(input('(0 입력시 종료)플레이어 1 순서, 입력할 숫자는? '))
    except:
        print('정수를 입력하세요.')
        continue
    else:
        if p1==list[0]:
            del list[0]
            continue
        elif p1==0:
            for i in range(len(list)):
                print(list[i],end=' ')
            print()
        else:
            print('잘못된 숫자를 입력했습니다. 다시 입력하세요.')
            continue

    while True:
        if list[0]==31:
            break
        try:
            p2=int(input('(0 입력시 종료)플레이어 2 순서, 입력할 숫자는? '))
        except:
            print('정수를 입력하세요.')
            continue
        else:
            if p2==list[0]:
                del list[0]
                continue
            elif p2==0:
                for i in range(len(list)):
                    print(list[i],end=' ')
                print()
                break
            else:
                print('잘못된 숫자를 입력했습니다. 다시 입력하세요.')
                continue
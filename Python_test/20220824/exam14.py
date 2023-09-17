# 실습 14 - 홀수 짝수 생성하기

# 1,2 아니면 다시 묻기
# 0은 종료

while True:
    num=input('홀수는 1, 짝수는 2를 입력해주세요 : ')
    if num=='':
        print('값을 입력하세요.')
    elif '.' in num:
        print('실수는 사용할 수 없습니다.')
    elif num=='0':
            print('종료합니다.')
            break
    else:    
        if num=='1' or num=='2':
            i=1
            for i in range(int(num),101,2):
                print(i,end=' ')
                i+=1
            print()
        else:
            print('다시 입력하세요.')
            continue

# 풀이

# num=int(input('홀수는 1, 짝수는 2를 입력해주세요 : '))

# for i in range(num,101,2):
#     print(i, end=' ')
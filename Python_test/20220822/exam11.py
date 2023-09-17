# 실습 11 - 홀수 짝수 구분하기

num=(input('양의 정수를 입력하세요 : '))
check_num=bool(num)

if check_num:   
    if float(num)>0:
        if float(num)%2==1:
            print('홀수입니다.')
        if float(num)%2==0:
            print('짝수입니다.')
        if 0<float(num)%1<1:
            print('실수는 입력할 수 없습니다.')
    else:
        print('양의 정수가 아닙니다.')
else:
    print('값을 입력하세요.')


# 풀이

num=(input('양의 정수를 입력하세요 : '))

check_dot=num.find('.')
# print(check_dot)

# 정수 여부 확인
if check_dot==-1:

    # check_num=bool(num)
    len_num=len(num)

    if len_num>0:
        if int(num)>=0:
            # print('양의 정수')
            if int(num)%2==0:
                print('짝수입니다.')
            else:
                print('홀수입니다.')
        else:
            print('양의 정수가 아닙니다.')
    else:
        print('값을 입력하지 않았습니다.')
else:
    print('실수형은 입력할 수 없습니다.')
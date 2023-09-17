# 실습 13 - 입대 영장 발급

gen=input('[남], [여] 중 하나를 입력하세요 : ')
if gen=='남':
    age=input('현재 나이를 입력하세요 : ')
    if int(age)>=20:
        sch=input('[재], [휴] 중 하나를 입력하세요 : ')
        if sch=='재':
            print('군대에 입대하십시오.')
        elif sch=='휴':
            print('종료합니다.')
        else:
            print('다시 입력하세요.')
    elif 0<int(age)<20:
        print('종료합니다.')
    else:
        print('다시 입력하세요.')
elif gen=='여':
    print('종료합니다.')
else:
    print('다시 입력하세요.')


# 풀이

gen=input('[남], [여] 중 하나를 입력하세요 : ')
if gen=='남':
    age=int(input('현재 나이를 입력하세요 : '))
    if int(age)>=20:
        sch=input('[재], [휴] 중 하나를 입력하세요 : ')
        if sch=='재':
            print('군대에 입대하십시오.')
        else:
            print('종료합니다.')
    else:
        print('종료합니다.')
else:
    print('종료합니다.')
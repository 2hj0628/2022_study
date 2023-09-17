# 실습 13 - 입대 영장 발급

try:
    gen=str(input('[남], [여] 중 하나를 입력하세요 : '))
    if gen=='남':
        age=int(input('현재 나이를 입력하세요 : '))
        if age>=20:
            sch=input('[재], [휴] 중 하나를 입력하세요 : ')
            if sch=='재':
                print('군대에 입대하십시오.')
    if gen!='남' and gen!='여' and age<0 and sch!='재' and sch!='휴':
        raise
except:
    print('다시 입력하세요.')
else:
    if gen=='여' or age<20 or sch=='휴':
        print('종료합니다.')
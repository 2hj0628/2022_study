# 실습 5 - 예방접종

try:
    age=int(input('아이가 태어난 지 몇 개월입니까? '))
    if age<0 or age>15:
        raise
except ValueError:
    print('다시 입력하세요.')
except:
    print('접종 대상자가 아닙니다.')
else:
    if 0<=age<=1:
        print('결핵 예방접종 대상자입니다.')
    if 0<=age<=2:
        print('B형간염 예방접종 대상자입니다.')
    if 2<=age<=6:
        print('파상풍 예방접종 대상자입니다.')
    if 2<=age<=15:
        print('폐렴구균 예방접종 대상자입니다.')
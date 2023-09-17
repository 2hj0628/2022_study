# 실습 7 - 수능 평균 등급

grade=float(input('수능 평균 등급 : '))

# case 1
if 1<=grade<=2:
    print('수능 최저 기준을 만족합니다.\n합격입니다.')
elif 2<grade<=9:
    print('수능 최저 기준을 만족하지 않습니다.\n불합격입니다.')
else:
    print('다시 입력하십시오.')

# case 2
if 1<=grade<=9:
    if 1<=grade<=2:
        print('수능 최저 기준을 만족합니다.\n합격입니다.')
    if 2<grade<=9:
        print('수능 최저 기준을 만족하지 않습니다.\n불합격입니다.')
else:
    print('다시 입력하십시오.')


# 풀이

# 수능 등급 1~9등급(소수점 포함)
grade=float(input('수능 평균 등급 : '))

if 1.0<=grade<10.0:
    if grade<=2.0:
        print('수능 최저 기준을 만족합니다.\n합격입니다.')
    else:
        print('수능 최저 기준을 만족하지 않습니다.\n불합격입니다.')
else:
    print('수능 등급은 1~9등급만 사용 가능합니다.')
# 실습 7 - 수능 평균 등급

try:
    grade=float(input('수능 평균 등급 : '))
    if grade<1 or grade>9:
        raise
except:
    print('다시 입력하세요.')
else:
    if 1<=grade<=2:
        print('수능 최저 기준을 만족합니다.\n합격입니다.')
    elif 2<grade<=9:
        print('수능 최저 기준을 만족하지 않습니다.\n불합격입니다.')

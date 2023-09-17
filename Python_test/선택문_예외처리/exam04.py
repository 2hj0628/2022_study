# 실습 4 - 15세 이상 등급 판정

msg=['이 등급의 영화를 볼 수 있습니다.','이 등급의 영화를 볼 수 없습니다.']
try:
    age=(int(input('당신의 나이는? ')))
    if age<=0:
        raise
except:
    print('잘못입력하였습니다.')
else:
    if age<15:
        print(msg[1])
    else:
        print(msg[0])
# 실습 4 - 15세 이상 등급 판정

# case 1
age=(int(input('당신의 나이는? ')))

if age>=15:
    print('이 등급의 영화를 볼 수 있습니다.')
elif age<=0:
    print('잘못입력하였습니다.')
else:
    print('이 등급의 영화를 볼 수 없습니다.')

# case 2
age=(int(input('당신의 나이는? ')))

msg=['이 등급의 영화를 볼 수 있습니다.','이 등급의 영화를 볼 수 없습니다.','잘못입력하였습니다.']

if age>=15:
    print(msg[0])
elif age<=0:
    print(msg[2])
else:
    print(msg[1])

# 풀이
age=int(input('당신의 나이는? '))

if age>=0:
    if age>=15:
        print('이 등급의 영화를 볼 수 있습니다.')
    else:
        print('이 등급의 영화를 볼 수 없습니다.')
else:
    print('잘못입력하였습니다.')
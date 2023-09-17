# 실습 8 - 경찰 체력 검정

# 모두 8점 이상을 맞아야 합격 가능성이 높은것으로 출력
# 커트라인: 13.6, 237 이내/ 51, 56, 46 이상

try:
    run_100=float(input('100m 기록(초) : '))
    run_1000=float(input('1000m 기록(초) : '))
    sit=int(input('윗몸일으키기 기록(회) : '))
    grip=int(input('좌우 악력 기록(kg) : '))
    push=int(input('팔굽혀펴기 기록(회) : '))

    health=[run_100,run_100,sit,grip,push]
    if run_100<0 or run_100<0 or sit<0 or grip<0 or push<0:
        raise
except:
    print('다시 입력하세요.')
else:
    if health[0]<=13.6 and health[1]<=237 and health[2]>=51 and health[3]>=56 and health[4]>=46:
        print('합격 가능성이 매우 높습니다.')
    else:
        print('합격 가능성이 낮습니다.')
# 실습 8 - 경찰 체력 검정

# 모두 8점 이상을 맞아야 합격 가능성이 높은것으로 출력
# 커트라인: 13.6, 237 이내/ 51, 56, 46 이상

run_h=float(input('100m 기록(초) : '))
run_th=float(input('1000m 기록(초) : '))
sit=int(input('윗몸일으키기 기록(회) : '))
grip=int(input('좌우 악력 기록(kg) : '))
push=int(input('팔굽혀펴기 기록(회) : '))

health=[run_h,run_th,sit,grip,push]
msg=['합격 가능성이 매우 높습니다.','합격 가능성이 낮습니다.']

if 0<health[0]<=13.6:
    if 0<health[1]<=237:
        if health[2]>=51:
            if health[3]>=56:
                if health[4]>=46:
                    print(msg[0])
                else:    
                    print(msg[1])    
            else:    
                print(msg[1])        
        else:    
            print(msg[1])
    else:    
        print(msg[1])
else:    
    print(msg[1])

# 풀이
m100=float(input('100m 기록(초) : '))
m1000=float(input('1000m 기록(초) : '))
sit_up=int(input('윗몸일으키기 기록(회) : '))
grip=float(input('좌우 악력 기록(kg) : '))
push_up=int(input('팔굽혀펴기 기록(회) : '))

if (m100>=0 and m1000>=0 and sit_up>=0 and 
    grip>=0 and push_up>=0):
    # print('정상기록')
    if (m100<=13.6 and m1000<=237 and sit_up>=51 and 
        grip>=56 and push_up>=46):
        print('합격 가능성이 매우 높습니다.')
    else:
        print('합격 가능성이 낮습니다.')
else:
    print('다시 기록해주에요.')
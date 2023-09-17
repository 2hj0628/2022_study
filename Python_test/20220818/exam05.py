# 실습 5 - 예방접종

age=int(input('아이가 태어난 지 몇 개월입니까? '))

dis=['결핵','B형간염','파상풍','폐렴구균']
msg='예방접종 대상자입니다.'

if age==0 or age==1:
    print(dis[0],msg)
    print(dis[1],msg)
elif age==2:
    print(dis[1],msg)
    print(dis[2],msg)
    print(dis[3],msg)
elif age>=3 and age<=6:
    print(dis[2],msg)
    print(dis[3],msg)
elif age>=7 and age<=15:
    print(dis[3],msg)
else:
    print('접종 대상자가 아닙니다.')

# 풀이

age=int(input('아이가 태어난 지 몇 개월입니까? '))

if 0<=age<=15:
    if 0<=age<=1:
        print('결핵 예방접종 대상자입니다.')
    if 0<=age<=2:
        print('B형간염 예방접종 대상자입니다.')
    if 2<=age<=6:
        print('파상풍 예방접종 대상자입니다.')
    if 2<=age<=15:
        print('폐렴구균 예방접종 대상자입니다.')
else:
    print('접종 대상자가 아닙니다.')
# 실습 10 - 주인공 체력 계산하기

# 종료 자동
# 음수x
# 실수x

hp=100
damage=0
while True:
    print('주인공의 체력은',hp,'입니다.')
    damage=input('얼마의 데미지를 입히시겠습니까 : ')
    if damage=='':
        print('값을 입력하세요.')
    elif '.' in damage:
        print('실수는 입력할 수 없습니다.')
    else:
        new_damage=int(damage)
        if new_damage<1:
            print('다시 입력하세요.')
            continue
        0<new_damage
        hp=hp-new_damage
        if hp<=0:
            print('주인공은 죽었습니다.')
            break


# 풀이
# hp=100
# while hp>0:
#     print('주인공의 체력은',hp,'입니다.')
#     damage=int(input('얼마의 데미지를 입히시겠습니까 : '))
#     hp-=damage
# print('주인공은 죽었습니다.')
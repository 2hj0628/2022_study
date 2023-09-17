# 실습 10 - 주인공 체력 계산하기

# 종료 자동
# 음수, 실수x

hp=100
while hp>0:
    print('주인공의 체력은',hp,'입니다.')
    try:
        damage=int(input('얼마의 데미지를 입히시겠습니까 : '))
        hp-=damage
        if damage<0:
            raise
    except:
        print('다시 입력하세요.')
print('주인공은 죽었습니다.')
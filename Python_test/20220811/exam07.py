# 실습 7 - 원의 둘레와 넓이 구하기
# 처리조건 : 둘레와 넓이의 소수점 1번째 자리까지만 표현

ban=int(input('원의 반지름을 입력하세요(cm) :'))
dul=round(float(ban*2*3.14),1)
nul=round(float(ban**2*3.14),1)
print('원의 둘레는',dul,'cm이고 원의 넓이는',nul,'입니다')

# 풀이
r=float(input('원의 반지름을 입력하세요(cm) :'))

rod=2*3.14*r
area=round(3.14*(r**2),1)

print('원의 둘레는',rod,'cm이고 원의 넓이는',area,'입니다')
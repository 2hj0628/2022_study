# 실습 9 - BMI 계산하기

# 입력
name=input('이름을 입력하세요 :')
height=int(input('키(cm)를 입력하세요 :'))
weight=int(input('몸무게(kg)를 입력하세요 :'))

# 처리
new_height=height//100+height%100/100
bmi=round(float(weight/(new_height**2)),2)

# 출력
print(name+'님의 키는',height,'cm이고 몸무게는',weight,'kg입니다.')
print('BMI 지수는',bmi,'입니다.')
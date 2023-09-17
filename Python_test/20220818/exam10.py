# 실습 10 - BMI 계산하기

# bmi=kg/㎡
# 18.5미만:저체중 / 22.9이하:정상 / 24.9이하:과체중 / 29.9이하:비만 / 30이상:고도비만

# 입력
name=input('이름을 입력하세요 : ')
height=float(input('키(cm)를 입력하세요 : '))
weight=float(input('몸무게(kg)를 입력하세요 : '))

# 처리
bmi=round(weight/((height/100)**2),2)
obe=['저체중','정상','과체중','비만','고도비만']
msg='{}님의 키는 {}cm이고 몸무게는 {}kg입니다.\nBMI 지수는 {}입니다.'.format(name,height,weight,bmi)

# 출력
if 0<=height and 0<=weight:
    if bmi<18.5:
        print(msg,obe[0],'입니다.')
    if 18.5<=bmi<=22.9:
        print(msg,obe[1],'입니다.')
    if 23<=bmi<=24.9:
        print(msg,obe[2],'입니다.')
    if 25<=bmi<=29.9:
        print(msg,obe[3],'입니다.')
    if bmi>=30:
        print(msg,obe[4],'입니다.')
else:
    print('잘못입력하였습니다.')

# 풀이

name=input('이름을 입력하세요 : ')
height=input('키(cm)를 입력하세요 : ')
weight=input('몸무게(kg)를 입력하세요 : ')
# print(bool(name))

check_name=bool(name)
check_height=bool(height)
check_weight=bool(weight)


if check_name and check_height and check_weight:
    # 몸무게와 키가 양수인지 여부 판별
    if float(weight)>=0 and int(height)>=0:
        # 정수와 실수형으로 타입을 변경
        bmi=float(weight)/(int(height)/100)**2

        if bmi>=30:
            result='고도비만'
        # if 25<=bmi<30:    #elif일 경우, 비효율적
        elif bmi>=25:
            result='비만'
        elif bmi>=23:
            result='과체중'
        elif bmi>=18.5:
            result='정상'
        else:
            result='저체중'

        print(name+'님의 키는 ',height,'cm이고 몸무게는 ',weight,'kg 입니다.')
        print('BMI 지수는 ',round(bmi,2),'입니다.',result,'입니다.')
    else:
        print('키와 몸무게는 음수 값이 올 수 없습니다.')
else:
    print('입력하지 않은 항목이 존재하여 종료합니다.')
# 실습 10 - BMI 계산하기

# bmi=kg/㎡
# 18.5미만:저체중 / 22.9이하:정상 / 24.9이하:과체중 / 29.9이하:비만 / 30이상:고도비만

try:
    name=input('이름을 입력하세요 : ')
    height=float(input('키(cm)를 입력하세요 : '))
    weight=float(input('몸무게(kg)를 입력하세요 : '))

    bmi=round(weight/((height/100)**2),2)
    obe=['저체중','정상','과체중','비만','고도비만']
    msg='{}님의 키는 {}cm이고 몸무게는 {}kg입니다.\nBMI 지수는 {}입니다.'.format(name,height,weight,bmi)

    if height<=0 or weight<=0:
        raise
except:
    print('잘못입력하였습니다.')
else:
    if bmi<18.5:
        print(msg,obe[0],'입니다.')
    elif bmi<=22.9:
        print(msg,obe[1],'입니다.')
    elif bmi<=24.9:
        print(msg,obe[2],'입니다.')
    elif bmi<=29.9:
        print(msg,obe[3],'입니다.')
    else:
        print(msg,obe[4],'입니다.')
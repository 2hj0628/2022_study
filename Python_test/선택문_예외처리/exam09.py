# 실습 9 - 공무원 시험 과락 판별

try:
    kor=int(input('국어 점수 : '))
    eng=int(input('영어 점수 : '))
    his=int(input('한국사 점수 : '))
    sel1=int(input('선택과목1 점수 : '))
    sel2=int(input('선택과목2 점수 : '))

    sub=[kor,eng,his,sel1,sel2]

    for i in range(5):
        if sub[i]<0 or sub[i]>100:
            raise
        
except:
    print('다시 입력하세요.')
else:
    for i in range(5):
        if sub[i]>=40:
            print('과락 아님')
    else:
        print('과락')
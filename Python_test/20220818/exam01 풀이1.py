# 실습 1 - 총점과 평균 구하기

print('총점과 평균 구하기')
print('점수는 0~100사이의 양의 정수만 입력가능합니다.')

kor=int(input('국어 점수 : '))
eng=int(input('영어 점수 : '))
math=int(input('수학 점수 : '))

# case 1
# if (kor>=0 and kor<=100) and (eng>=0 and eng<=100) and (math>=0 and math<=100):
#     sum=kor+eng+math
#     avg=round(float(sum/3),1)
#     print('총점은 {0}점이고, 평균은 {1}점입니다.'.format(sum,avg))
# else:
#     print('점수는 0~100사이의 양의 정수만 가능합니다.')

# case 2
if(kor>=0 and kor<=100):
    if(eng>=0 and eng<=100):
        if(math>=0 and math<=100):
            sum=kor+eng+math
            avg=round(float(sum/3),1)
            print('총점은 {0}점이고, 평균은 {1}점입니다.'.format(sum,avg))
        else:
            print('수학 점수는 0~100사이의 양의 정수만 가능합니다.')
    else:
        print('영어 점수는 0~100사이의 양의 정수만 가능합니다.')        
else:
    print('국어 점수는 0~100사이의 양의 정수만 가능합니다.')
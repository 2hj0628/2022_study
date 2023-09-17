# 실습 1 - 총점과 평균 구하기

# 입력
try:
    kor=int(input('국어 점수 : '))
    eng=int(input('영어 점수 : '))
    math=int(input('수학 점수 : '))
    sum=kor+eng+math
    avg=round(sum/3,1)
    if kor<0 or eng<0 or math<0 or kor>100 or eng>100 or math>100:
        raise
except ValueError:
    print('다시 입력하세요.')
except:
    print('0~100사이의 수만 입력하세요.')
else:
    print('총점은',str(sum)+'점이고, 평균은',str(avg)+'점입니다.')

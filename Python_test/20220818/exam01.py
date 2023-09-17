# 실습 1 - 총점과 평균 구하기

# 입력
kor=int(input('국어 점수 : '))
eng=int(input('영어 점수 : '))
math=int(input('수학 점수 : '))

# 처리
sum=kor+eng+math
aver=round(sum/3,1)

# 출력
# if 0<=kor<=100 and 0<=eng<=100 and 0<=math<=100:
#     print('총점은',str(sum)+'점이고, 평균은',str(aver)+'점입니다.')
# else:
#     print('다시 입력하시오.')

# if kor<0 or kor>100:
#     if eng<0 or eng>100:
#         if math<0 or math>100:
#             print('다시 입력하시오.')
# else:
#     print('총점은',str(sum)+'점이고, 평균은',str(aver)+'점입니다.')

if kor<0 or eng<0 or math<0 or kor>100 or eng>100 or math>100:
    print('다시 입력하시오.')
else:
    print('총점은',str(sum)+'점이고, 평균은',str(aver)+'점입니다.')
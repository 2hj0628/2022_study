# 실습 1 - 총점과 평균 구하기

# subject list
# 0:국어, 1:영어, 2:수학
subject=['국어','영어','수학']

# score list
# 0:국어, 1:영어, 2:수학
score=list()
score.append(int(input(subject[0]+' 점수 : ')))
score.append(int(input(subject[1]+' 점수 : ')))
score.append(int(input(subject[2]+' 점수 : ')))

msg=' 점수는 0~100사이의 양의 정수만 가능합니다.'

if(score[0]>=0 and score[0]<=100):
    if(score[1]>=0 and score[1]<=100):
        if(score[2]>=0 and score[2]<=100):
            sum=score[0]+score[1]+score[2]
            avg=round(float(sum/3),1)
            print('총점은 {0}점이고, 평균은 {1}점입니다.'.format(sum,avg))
        else:
            print(subject[2]+msg)
    else:
        print(subject[1]+msg)        
else:
    print(subject[0]+msg)
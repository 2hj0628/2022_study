# 실습 12 - 합격 판별하기

# 예외처리할 것 없음

grade=[75,83,95,99,67,55]

print('2022 제 3회 한국사 시험 결과')
for i in range(5):
    i+=1
    if grade[i]>=70:
        print(i,'번 학생은 1급 입니다.')
    elif grade[i]>=60:
        print(i,'번 학생은 2급 입니다.')
    else:
        print(i,'번 학생은 불합격 입니다.')
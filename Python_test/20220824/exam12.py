# 실습 12 - 합격 판별하기

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


# while i<6:
#     i+=1
    


# 풀이

# case 1
# score=[75,83,95,99,67,55]
# idx=0

# for i in score:
#     idx+=1
#     if i>=70:
#         print(idx,'번 학생은 1급입니다.')
#     elif i>=60:
#         print(idx,'번 학생은 2급입니다.')
#     else:
#         print(idx,'번 학생은 불합격입니다.')

# case 2

# score=[75,83,95,99,67,55]

# for i in range(6):
#     if score[i]>=70:
#         print(i+1,'번 학생은 1급입니다.')
#     elif score[i]>=60:
#         print(i+1,'번 학생은 2급입니다.')
#     else:
#         print(i+1,'번 학생은 불합격입니다.')
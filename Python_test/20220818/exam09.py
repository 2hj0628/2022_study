# 실습 9 - 공무원 시험 과락 판별

kor=int(input('국어 점수 : '))
eng=int(input('영어 점수 : '))
his=int(input('한국사 점수 : '))
sel1=int(input('선택과목1 점수 : '))
sel2=int(input('선택과목2 점수 : '))

sub=[kor,eng,his]
sub_sel=[sel1,sel2]

if (0<=sub[0]<=100 and 0<=sub[1]<=100 and 
    0<=sub[2]<=100 and 0<=sub_sel[0]<=100 and
    0<=sub_sel[1]<=100):
    if (sub[0]>=40 and sub[1]>=40 and 
        sub[2]>=40 and sub_sel[0]>=40 and
        sub_sel[1]>=40):
        print('과락 아님')
    else:
        print('과락')
else:
    print('다시 입력하시오.')

# 풀이

# 필수 3과목 : 국어, 영어, 한국사
kor=float(input('국어 점수 : '))
eng=float(input('영어 점수 : '))
his=float(input('한국사 점수 : '))

# 선택 2과목
opt1=float(input('선택과목1 점수 : '))
opt2=float(input('선택과목2 점수 : '))

# 과락 여부
if 0<=kor<=100 and 0<=eng<=100 and 0<=his<=100 and 0<=opt1<=100 and 0<=opt2<=100:
    if kor<40 or eng<40 or his<40 or opt1<40 or opt2<40:
        print('과락')
    else:
        print('과락아님')
else:
    print('다시 입력하시오.')
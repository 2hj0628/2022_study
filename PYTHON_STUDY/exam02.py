'''
    {'이름':'라이언','국어':92,'수학':98,'영어':96,'과학':98},
    {'이름':'어피치','국어':87,'수학':98,'영어':85,'과학':98},
    {'이름':'무지',  '국어':98,'수학':92,'영어':96,'과학':92},
    {'이름':'콘',    '국어':76,'수학':96,'영어':94,'과학':90},
    {'이름':'춘식이','국어':64,'수학':88,'영어':92,'과학':92},
    {'이름':'제이지','국어':95,'수학':98,'영어':98,'과학':98}
'''
# 함수 선언
def create_student(name,korean,math,english,science):
    return {
        '이름':name,
        '국어':korean,
        '수학':math,
        '영어':english,
        '과학':science
    }

# 학생 리스트 생성
students=[
    create_student('라이언',92,98,96,98),
    create_student('어피치',87,98,85,98),
    create_student('무지',98,92,96,92),
    create_student('콘',76,96,94,90),
    create_student('춘식이',64,88,92,92),
    create_student('제이지',95,98,98,98)
]

print('이름','총점','평균',sep='\t')

for student in students:
    score_sum=student['국어']+student['수학']+student['영어']+student['과학']
    scroe_avg=score_sum/4
    print(student['이름'],score_sum,scroe_avg,sep='\t')
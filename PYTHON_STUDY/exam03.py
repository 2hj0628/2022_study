# 함수 선언
def create_student(name,korean,math,english,science):
    return {
        '이름':name,
        '국어':korean,
        '수학':math,
        '영어':english,
        '과학':science
    }

# 합계 구하는 함수
def get_sum(student):
    return student['국어']+student['수학']+student['영어']+student['과학']

# 평균 구하는 함수
def get_avg(student):
    return get_sum(student)/4

# 학생 성적을 출력하는 함수
def to_string(student):
    return '{}\t{}\t{}'.format(
        student['이름'],
        get_sum(student),
        get_avg(student)
    )

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
    print(to_string(student))
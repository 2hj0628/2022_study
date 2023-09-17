# 성적관리 프로그램 - 함수 적용

# 학생 등록(생성) 함수
def create_stu(name,kor,math,eng,sci):
    return{
        'name' : name,
        'kor' : kor,
        'math' : math,
        'eng' : eng,
        'sci' : sci
    }

# 학생 리스트
stus=[
    create_stu('라이언',80,90,99,97),
    create_stu('어피치',100,85,100,93),
    create_stu('무지',70,75,60,76)

    # {'name':'라이언','kor':80,'math':90,'eng':99,'sci':97},
    # {'name':'어피치','kor':100,'math':85,'eng':100,'sci':93},
    # {'name':'무지','kor':70,'math':75,'eng':60,'sci':76}
]

# 총점 구하는 함수
def get_sum(stu):
    return stu['kor']+stu['math']+stu['eng']+stu['sci']

# 평균 구하는 함수
def get_avg(stu):
    return get_sum(stu)/4

# 이름, 총점과 평균 출력하는 함수
def stu_info(stu):
    return '{}\t{}\t{}'.format(stu['name'],get_sum(stu),get_avg(stu))

# 학생을 한명씩 반복해서 출력
print('이름','총점','평균',sep='\t')
for stu in stus:
    print(stu_info(stu))
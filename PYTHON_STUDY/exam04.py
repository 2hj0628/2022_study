class Student:
    
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

    # 합계 구하는 함수
    def get_sum(self):
        return self.korean+self.math+self.english+self.science

    # 평균 구하는 함수
    def get_avg(self):
        return self.get_sum()/4

    # 학생 성적을 출력하는 함수
    def to_string(self):
        return '{}\t{}\t{}'.format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )


# 학생 리스트 생성
students=[
    Student('라이언',92,98,96,98),
    Student('어피치',87,98,85,98),
    Student('무지',98,92,96,92),
    Student('콘',76,96,94,90),
    Student('춘식이',64,88,92,92),
    Student('제이지',95,98,98,98)
]

print('이름','총점','평균',sep='\t')

for student in students:
    print(student.to_string())

# for i in students:
#     print(i.name)
#     print(i.korean)
#     print(i.math)
#     print(i.english)
#     print(i.science)
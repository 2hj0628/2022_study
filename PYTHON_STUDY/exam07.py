class Student:
    
    # 클래스 변수
    count=0
    students=[]

    def __init__(self,name,korean,math,english,science):
        # 인스턴스 변수
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
        Student.count+=1
        Student.students.append(self)

    # 합계 구하는 함수
    def get_sum(self):
        return self.korean+self.math+self.english+self.science

    # 평균 구하는 함수
    def get_avg(self):
        return self.get_sum()/4

    # 학생 성적을 출력하는 함수
    def __str__(self):
        return '{}\t{}\t{}'.format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )

    @classmethod  # 얘빼곤 다 인스턴스메소드
    def print(cls):
        print('--- 학생 목록 ---')
        print('이름','총점','평균',sep='\t')
        for student in cls.students:
            print(str(student))  # str안써도 됨

Student('라이언',92,98,96,98),
Student('어피치',87,98,85,98),
Student('무지',98,92,96,92),
Student('콘',76,96,94,90),
Student('춘식이',64,88,92,92),
Student('제이지',95,98,98,98)

Student.print()  # Student 클래스에서 print함수 부름
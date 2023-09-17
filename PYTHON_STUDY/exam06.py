class Student:
    
    # 클래스 변수
    count=0

    def __init__(self,name,korean,math,english,science):
        # 인스턴스 변수
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

        Student.count+=1
        print('{}번째 학생이 등록되었습니다.'.format(Student.count))

# 학생 리스트 생성
students=[
    Student('라이언',92,98,96,98),
    Student('어피치',87,98,85,98),
    Student('무지',98,92,96,92),
    Student('콘',76,96,94,90),
    Student('춘식이',64,88,92,92),
    Student('제이지',95,98,98,98)
]


print('현재 학생수는 {}명입니다.'.format(Student.count))
from Stu_class import Stu     #from 파일명 import 클래스
# from A : A파일로부터
# import A : A클래스를 호출

# 학생 리스트
stus=[
    Stu('라이언',80,90,99,97),
    Stu('어피치',100,85,100,93),
    Stu('무지',70,75,60,76)
]

# 학생을 한명씩 반복해서 출력
print('이름','총점','평균',sep='\t')
for stu in stus:
    print(stu.to_string())
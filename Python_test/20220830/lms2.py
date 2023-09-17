# 성적관리 프로그램 - 클래스 사용
class Stu:
    # 학생 등록(생성)
    def __init__(self,name,kor,math,eng,sci):
        self.name=name
        self.kor=kor
        self.math=math
        self.eng=eng
        self.sci=sci

    # 총점 구하기
    def get_sum(self):
        return self.kor+self.math+self.eng+self.sci

    # 평균 구하기
    def get_avg(self):
        return round(self.get_sum()/4,2)    #호출할땐 self X

    # 정보 출력
    def to_string(self):
        return '{}\t{}\t{}'.format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )

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
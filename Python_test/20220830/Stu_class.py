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
        return round(self.get_sum()/4,2)    #호출할땐 selfX

    # 정보 출력
    def to_string(self):
        return '{}\t{}\t{}'.format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )
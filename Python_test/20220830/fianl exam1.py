# final exam 1 - 학생관리 프로그램

# 우대사항 : 객체지향, 오류 처리

# 요구사항
# 1.반별로 학생관리하는 프로그램
# 2.학생은 학번, 이름, 성적을 가짐
# 3.학생을 추가 / 제거 / 이름 변경하는 기능
# 4.학번을 입력받아 학생정보를 출력하는 기능
# 5.학생 추가시 학번 중복되면 학번만 다시 받는 기능
# 6.반 추가기능
# 7.현재 반의 개수를 출력하는 기능

# 학생관리_프로그램.zip 9/5까지 실습란에 업로드

class student:
    def __init__(self,st_name,st_number,st_score):
        self.st_name=st_name
        self.st_number=st_number
        self.st_score=st_score
    def info(self):
        return '{}\t{}\t{}'.format(
            self.st_name,
            self.st_number,
            self.st_score
        )

students=[]
# ValueError int에서 문자열 넣을때
# TypeError 문자열에 int 더할때

while True:
    num=int(input('1.학생조회 2.학생추가 3.학생 이름변경 4.학생제거 5.반조회 0.종료 : '))
    if num==1:
        name=input('이름을 입력하세요 : ')
        for i in range(len(students)):
            if name in students[i][0]:
                print(students[i])
            else:
                print('등록되지 않은 학생입니다.')
        break
    elif num==2:
        name=input('이름을 입력하세요 : ')
        number=int(input('학번을 입력하세요 : ')) #학번중복시 다시입력
        for i in range(len(students)):
            if number in students[i][1]:
                break
            else:
                print('중복된 학번입니다. 다시 입력하세요.')
        score=int(input('성적을 입력하세요 : '))
        room=input('반을 입력하세요 : ')   #기존에 없는 반이면 자동 추가
        students.append([name,number,score,room])
    elif num==3:
        name=input('이름을 입력하세요 : ')
        name_fix=input('변경할 이름을 입력하세요 : ')
        for i in range(len(students)):
            if name in students[i][0]:
                students[i][0]=name_fix
        # room=input('반을 입력(변경)하세요 : ')
    elif num==4:
        name=input('이름을 입력하세요 : ')
        for i in range(len(students)):
            if name in students[i][0]:
                del students[i]
    elif num==5:
        print('반의 개수는',students.count(room),'개 입니다.')
        room=input('조회하고 싶은 반을 입력하세요 : ')
        for i in range(len(students)):
            if room in students[i][3]:
                print(students[i])
    elif num==0:
        break
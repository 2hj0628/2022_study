# 성적관리 프로그램
# 학생 리스트
stus=[
    {'name':'라이언','kor':80,'math':90,'eng':99,'sci':97},
    {'name':'어피치','kor':100,'math':85,'eng':100,'sci':93},
    {'name':'무지','kor':70,'math':75,'eng':60,'sci':76}
]

# 학생을 한명씩 반복해서 출력
print('이름','총점','평균',sep='\t')
for stu in stus:
    sum=stu['kor']+stu['math']+stu['eng']+stu['sci']
    avg=sum/4
    print(stu['name'],sum,avg,sep='\t')
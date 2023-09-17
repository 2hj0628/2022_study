# 학생이 여러 명일 때

stus=[
    {'name':'라이언','number':202201,'age':21},
    {'name':'어피치','number':202202,'age':22},
    {'name':'춘식이','number':202203,'age':23},
]

# for i in range(3):
#     print(stus[i]['age'])

# 나이 평균 구하기
age_sum=0
for stu in stus:
    age_sum+=stu['age']
    
print(int(age_sum/len(stus)))
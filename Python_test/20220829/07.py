# 학생이 여러 명일 때

stus=[
    {'name':'라이언','number':202201,'age':21},
    {'name':'어피치','number':202202,'age':22},
    {'name':'춘식이','number':202203,'age':23},
]

# 나이 총합 구하는 함수 정의
def sum_age(stus):
    temp=0
    for i in stus:
        temp+=i['age']
    return temp

# 나이 평균 구하는 함수 정의
# 함수 안에 다른 함수를 호출
def avg_age(stus):
    return int(sum_age(stus)/len(stus))

# 나이 총합 구하는 함수 호출=66
sum=sum_age(stus)
print(sum)

# 나이 평균 구하는 함수 호출=22
avg=avg_age(stus)
print(avg)
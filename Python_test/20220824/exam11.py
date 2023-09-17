# 실습 11 - 끼니 계산하기

num=''
i=0
meal=['아침','점심','저녁','야식']

while num!=0:
    num=input("(종료 '0')며칠이 지났습니까 : ")
    if num=='':
        print('값을 입력하세요.')
    elif '.' in num:
        print('실수는 입력할 수 없습니다.')
    else:
        if int(num)==0:
            break
        if int(num)<1:
            print('다시 입력하세요.')
        for i in range(int(num)):
            for j in meal:
                print(j)


# 풀이

# day=1
# i=0

# meal=['아침','점심','저녁','야식']

# while day!=0:
#     day=int(input("(종료 '0')며칠이 지났습니까 : "))
#     i=day
#     while i>0:
#         for j in meal:
#             print(j)
#         i-=1            #리스트 프린트 후 i-1>0? 맞으면 한번 더 출력
        
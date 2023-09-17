# 실습 9 - 가우스 계산기

while(True):
    num=input("(종료 '1')숫자 입력 : ")
    if num=='':
        print('값을 입력하세요.')
    elif '.' in num:
        print('실수는 입력할 수 없습니다.')
    else:
        new_num=int(num)
        if new_num<1:
            print('다시 입력하세요.')
            continue
        if new_num>=1:
            result=((new_num+1)*(new_num/2))
            print(round(result))
        if new_num==1:
            break


# 풀이

# num=0
# while num!=1:
#     num=int(input("(종료 '1')숫자 입력 : "))
#     i=1
#     sum=0
#     while i<num+1:
#         sum+=i
#         i+=1
#     print(sum)
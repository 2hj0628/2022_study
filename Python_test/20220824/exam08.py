# 실습 8 - 입력한 단을 출력하기

# 0, 음수,실수는 안됌
# 1 출력 후 종료

while True:
        num=input("(종료 '1')구구단 몇 단을 출력할까요 : ")
        if num=='':
                print('값을 입력하세요.')
        elif '.' in num:
                print('실수는 입력할 수 없습니다.')
        else:
                if int(num)<1:
                        print('다시 입력하세요.')
                        continue
                for i in range(10):
                        print(int(num),'X',i,'=',int(num)*i)
                        i+=1
                if int(num)==1:
                        break

# 풀이

# num=0
# while num!=1:
#     num=int(input("(종료 '1')구구단 몇 단을 출력할까요 : "))

#     i=1
#     while i<10:
#         print(num,'X',i,'=',num*i)
#         i+=1
# 실습 8 - 입력한 단을 출력하기

# 0, 음수,실수는 안됌
# 1 출력 후 종료

num=0
while num!=1:
        try:
                num=int(input("(종료 '1')구구단 몇 단을 출력할까요 : "))
                if num<0:
                        raise
        except:
                print('다시 입력하세요.')
        else:
                for i in range(10):
                        print(num,'X',i,'=',num*i)
                        i+=1
num=['3','안녕하세요','4',2,10,'좋아요']
digit_num=[]

for i in num:
    try:
        digit_num.append(int(i))
    except:
        pass

print(digit_num)
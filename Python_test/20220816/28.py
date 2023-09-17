# 반복문에서의 사전

dict1={'a':1,'b':2,'c':3}

for i in dict1.keys():  #=for i in dict1:
    print(i)    #콜론, 들여쓰기 필수, 키만 나옴
print()

for i in dict1.values():
    print(i)    #값만 나옴
print()

for i in dict1.items():
    print(i)
print()
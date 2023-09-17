# key : 변수 또는 튜플
# value : 거의 모든 자료형 가능
# key는 변경 불가능, value는 변경 가능
# set{}는 순서x 중복x

num=1

d={
    num:['리','스','트','트'],
    (2,'나'):(2,'나','나'),
    # [1,2,3]:['a','b','c']
    3:{'A','B','D','D'}
}
print(d)
print(d[num])
print(d[(2,'나')])
print(d[3])
# 가변 매개변수

def func(a,c=1,*arg,d=12):
    print(a,arg,c)

func(1)
func(2,3)
func(2,3,4,5,6)
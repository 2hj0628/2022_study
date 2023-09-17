# 키워드 매개변수
# 매개변수를 키워드로 지정

def func(a,b,c,d,e):  #기본값 때문에 e=1이 아닐때, d=1하면 에러
    print(a+b-c-d+e)

func(1,2,3,4,5)
func(5,4,3,2,1)
print()
func(a=1,b=2,c=3,d=4)
func(a=1,b=2,c=3,d=4,e=5)
func(e=5,d=4,c=3,b=2,a=1)
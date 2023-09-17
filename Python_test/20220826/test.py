print('이 파일은 모듈 생성하기 예제 파일입니다.')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

pi=3.14

__name__='test1'

# print(__name__)

if __name__=='__main__':
    print('이 구문은 매인일 때만 출력합니다.')
    print(add(pi,3))
# 실습 4 - 이름 묻고 출력하기

name=''
while name!='q':
    try:
        name=str(input('당신의 이름을 입력하세요. q를 입력하면 종료합니다. : '))
    except:
        print('다시 입력하세요.')
    else:   
        print(name)

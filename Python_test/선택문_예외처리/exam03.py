# 실습 3 - 반배치

list_class=['인공지능','빅데이터']
list_ai=['라이언','네오','춘식','튜브','프로도']
list_data=['어피치','무지','콘','제이지']
try:
    name=str(input('이름이 무엇입니까? '))
    if not name in list_ai:
        raise
except ValueError:
    print('다시 입력하세요.')
except:
    print('미등록자입니다.')
else:
    if name in list_ai:
        print(list_class[0],'클래스로 가시면 됩니다.')
    elif name in list_data:
        print(list_class[1],'클래스로 가시면 됩니다.')

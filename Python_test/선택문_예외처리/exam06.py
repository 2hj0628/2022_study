# 실습 6 - 본인 이름 확인

try:
    name=input('본인의 이름을 입력하세요 : ')
    key='2hj0628'
    if name!=key:
        raise
except:
    print('다시 입력하세요.')
else:
    print('확인되었습니다.')
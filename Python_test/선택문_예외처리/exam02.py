# 실습 2 - 도어락 비밀번호

try:
    password=int(input('비밀번호는 무엇입니까?'))
    if password!=1234:
        raise
except ValueError:
    print('다시 입력하세요.')
except:
    print('비밀번호가 틀렸습니다.')
else:
    print('문이 열렸습니다.')

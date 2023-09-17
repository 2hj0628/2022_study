# 실습 2 - 도어락 비밀번호

password=input('비밀번호는 무엇입니까?')
if password=='1234':
    print('문이 열렸습니다.')
else:
    print('비밀번호가 틀렸습니다.')

# 풀이

# case 1
door_lock=input('비밀번호는 무엇입니까?')
if door_lock=='1234':
    print('문이 열렸습니다.')

if door_lock!='1234':
    print('비밀번호가 틀렸습니다.')

# case 2
if door_lock=='1234':
    print('문이 열렸습니다.')
else:
    print('비밀번호가 틀렸습니다.')

# case 3
if door_lock!='1234':
    print('비밀번호가 틀렸습니다.')
else:
    print('문이 열렸습니다.')

# case 4
pwd='1234'
if door_lock==pwd:
    print('문이 열렸습니다.')
else:
    print('비밀번호가 틀렸습니다.')
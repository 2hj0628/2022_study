# 로그인 만들기

id=True
password=True

# case 1
if (id==True) and (password==True):
    print('로그인 되었습니다.')
else:
    print('아이디 또는 비밀번호가 틀립니다.')

# case 2
if id==True:
    if password==True:
        print('로그인 되었습니다.')
else:
    print('아이디 또는 비밀번호가 틀립니다.')

# case 3
if id:
    if password:
        print('로그인 되었습니다.')
else:
    print('아이디 또는 비밀번호가 틀립니다.')

# case 4
if id and password:
    print('로그인 되었습니다.')
else:
    print('아이디 또는 비밀번호가 틀립니다.')
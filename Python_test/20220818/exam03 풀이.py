# 풀이

# 인공지능 : 라이언, 네오, 춘식, 튜브, 프로도
# 빅데이터 : 어피치, 무지, 콘, 제이지

# 출력메시지
# 인공지능 클래스로 가시면 됩니다.
# 빅데이터 클래스로 가시면 됩니다.
# 미등록자입니다.


# case 1 - if문 사용
name=input('이름이 무엇입니까? ')

# 인공지능 클래스 판별
if name=='라이언':
    print('인공지능 클래스로 가시면 됩니다.')
if name=='네오':
    print('인공지능 클래스로 가시면 됩니다.')
if name=='춘식':
    print('인공지능 클래스로 가시면 됩니다.')
if name=='튜브':
    print('인공지능 클래스로 가시면 됩니다.')
if name=='프로도':
    print('인공지능 클래스로 가시면 됩니다.')

# 빅데이터 클래스 판별
if name=='어피치':
    print('빅데이터 클래스로 가시면 됩니다.')
if name=='무지':
    print('빅데이터 클래스로 가시면 됩니다.')
if name=='콘':
    print('빅데이터 클래스로 가시면 됩니다.')
if name=='제이지':
    print('빅데이터 클래스로 가시면 됩니다.')

# 수강생이 아닌 경우
if (name!='라이언'and name!='네오'and name!='춘식'and name!='튜브'and name!='프로도'
    and name!='어피치'and name!='콘'and name!='제이지'and name!='무지'):
    print('미등록자입니다.')


# case 2 - if elif else 문을 사용
name=input('이름이 무엇입니까? ')

if name=='라이언'or name=='네오'or name=='춘식'or name=='튜브'or name=='프로도':
    print('인공지능 클래스로 가시면 됩니다.')
elif name=='어피치'or name=='콘'or name=='제이지'or name=='무지':
    print('빅데이터 클래스로 가시면 됩니다.')
else:
    print('미등록자입니다.')


# case 3 - list 활용
ai=['라이언','네오','춘식','튜브','프로도']
big=['어피치','무지','콘','제이지']

name=input('이름이 무엇입니까? ')

if name in ai:
    print('인공지능 클래스로 가시면 됩니다.')
elif name in big:
    print('빅데이터 클래스로 가시면 됩니다.')
else:
    print('미등록자입니다.')


# case 4 - flag 변수 사용
ai=['라이언','네오','춘식','튜브','프로도']
big=['어피치','무지','콘','제이지']
msg=['인공지능 클래스로 가시면 됩니다.','빅데이터 클래스로 가시면 됩니다.','미등록자입니다.']
# 수강생 여부 판별(수강생:True, 기본값:False)
ai_student=False
big_student=False

# 입력
name=input('이름이 무엇입니까? ')

# 처리
if name in ai:
    ai_student=True
elif name in big:
    big_student=True

# 출력
if ai_student:
    print(msg[0])
elif big_student:
    print(msg[1])
else:
    print(msg[2])
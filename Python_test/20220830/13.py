# 강제로 예외 발생시키기

num=input('정수를 입력하세요 : ')
num=int(num)

if (num>0):
    raise Exception('Exception occured')
    # pass      #아직 구현 안된 경우 메시지 알려줌
else:
    print('음수입니다.')
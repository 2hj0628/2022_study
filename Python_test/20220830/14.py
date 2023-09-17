list1=['3','안녕하세요','4',2,10,'좋아요']

try:
    num=input('정수를 입력하세요 : ')
    num=int(num)
    print(num,'번째 요소는',list1[num],'입니다.')
except ValueError as msg:
    # print(msg)
    print('정수를 입력하세요.')
except IndexError as msg:
    # print(msg)
    print('리스트의 범위를 벗어났습니다.')
except Exception as msg:
    # print(msg)
    print('예상하지 못한 오류가 발생했습니다.')
else:       #에러가 안났을 때 무조건 출력
    print('파이썬 예외처리 수업입니다.')
finally:    #에러에 관계없이 무조건 출력
    print('수업을 마치겠습니다. 감사합니다.')
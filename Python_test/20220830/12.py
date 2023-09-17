list1=['3','안녕하세요','4',2,10,'좋아요']

try:
    num=input('정수를 입력해주세요 : ')
    num=int(num)
    print(num,'번째 요소는',list1[num],'입니다.')
# except Exception:     #위에 있음 최상위라 아래꺼 안됨
#     print('나는 최상위')
except ValueError:
    print('정수를 입력하세요.')
except IndexError:
    print('리스트의 범위를 벗어났습니다.')
except Exception:
    print('나는 최상위')

# rename() 함수로 파일 이름 변경
# 당연히 한번 바꾸면 존재하지 않는 이름이라 두번째엔 에러

import os
print(os.listdir('./'))
os.rename('a.txt','project1.txt')
print(os.listdir('./'))
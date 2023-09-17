# 해당 파일의 파일명과 경로명을 분리 반환

import os

# 파일명만 추출
print(os.path.basename('C:\\Coding\\Python_test\\a.txt'))
# 디렉토리만 추출
print(os.path.dirname('C:\\Coding\\Python_test\\a.txt'))
# 디렉토리 파일명 튜플 형태로 추출
print(os.path.split('C:\\Coding\\Python_test\\a.txt'))

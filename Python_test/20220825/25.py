# path.abspath()함수로 파일의 존재 유무와 관계없이 해당 파일의 절대 경로를 반환
# 파일이 없어도 생성 가능하므로, 파일을 입력할 때 주로 활용

import os

print(os.path.exists('a.txt'))
print(os.path.abspath('a.txt'))
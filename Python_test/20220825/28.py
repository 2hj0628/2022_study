# 드라이브, 확장자를 분리 반환

import os
# 드라이브 분리 반환
print(os.path.splitdrive('C:\\Coding\\Python_test\\a.txt'))
# 확장자 분리 반환
print(os.path.splitext('C:\\Coding\\Python_test\\a.txt'))
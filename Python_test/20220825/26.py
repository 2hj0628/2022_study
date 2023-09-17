# path.abspath() 함수 활용
# a.txt 만들어냄

import os

f=open(os.path.abspath('a.txt'),'w')
f.write('abcd')
f.close()
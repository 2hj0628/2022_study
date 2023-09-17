# 표준 출력 전환

import sys

f=open('a.txt','w')
sys.stdout=f
print('1234')
f.close()
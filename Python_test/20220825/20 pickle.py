# pickle 모듈로 파일을 저장할 때는 바이너리 형식으로 입출력 해야함
# wb, rb 모드

import pickle

f=open('a.txt','wb')
data={1:'python',2:'java'}
pickle.dump(data,f)
f.close()

f=open('a.txt','rb')
data=pickle.load(f)
f.close()

print(data)
print(type(data))
# 리스트로 저장하기

f=open('a.txt','w')
f.write('[1,2,3]')
f.close()

f=open('a.txt','r')
data=f.read()
f.close()

print(data)
print(type(data))
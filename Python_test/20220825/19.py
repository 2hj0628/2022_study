# 사전자료형(dict)로 저장된 데이터 읽어오기

f=open('b.txt','w')
f.write("{'a':1,'b':2}")
f.close()

f=open('b.txt','r')
data=f.read()
f.close()

print(data)
print(type(data))
# readline() 함수로 파일의 내용을 한줄씩 가져올 수 있음

data1=('1','2','3','4','\n')
data2=['a','b','c','d']

f=open('a.txt','w')
f.writelines(data1)
f.writelines(data2)
f.close()

f=open('a.txt','r')
print(f.readline())
print(f.readline())
f.close()
# writelines()함수 사용

t1=('1','2','3','4','\n')
list1=['1','2','c','d']

f=open('a.txt','w')
f.writelines(t1)
f.writelines(list1)
f.close()
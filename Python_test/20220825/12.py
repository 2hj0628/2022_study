# r모드로 파일 열기, read()함수로 파일의 전체 내용 불러오기

f=open('a.txt','w')
f.write('123')
f.close()

f=open('a.txt','r')
print(f.read())
f.close()
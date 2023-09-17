# w모드일 경우 파일을 새로 생성하며, 기존에 파일이 있다면 덮어쓰기 때문에 기존 내용이 사라짐

f=open('a.txt','w')
f.write('1234') 
f.close()

f=open('a.txt','w')
f.write('5678') 
f.close()
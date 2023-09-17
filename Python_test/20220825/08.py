# w모드와 기능은 똑같지만, x모드는 기존 파일이 있다면 오류 발생(덮어쓰기 방지)

f=open('c.txt','x')
f.write('good bye') 
f.close()
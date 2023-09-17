# 기존 파일에 새로운 내용을 추가하기 위해서는 a모드를 사용

f=open('a.txt','w')
f.write('1234') 
f.close()

f=open('a.txt','a')
f.write('5678') 
f.close()
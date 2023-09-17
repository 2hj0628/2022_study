# 해당 파일명으로 파일이 없더라도 a모드로 생성 가능

f=open('b.txt','a')
f.write('abcd') 
f.close()
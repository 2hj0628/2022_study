# 새로운 파일을 쓰기 위해 x모드도 사용 가능
# 파일이 이미 존재하면 오류 발생

f=open('c.txt','x')
f.write('hello') 
f.close()
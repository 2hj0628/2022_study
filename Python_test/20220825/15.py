# while + if 문 활용

f=open('a.txt','r')

while True:
    line=f.readline()
    if not line:
        break
    print(line)

f.close()
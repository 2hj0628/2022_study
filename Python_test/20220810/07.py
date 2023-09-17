# 표현식이 아닌 할당문은 할당할 수 없음

num2=10;num3=20
# num1=(num2=num2+num3)   #SyntaxError
num1=num2=num2+num3       #num1은 30이 할당
# num1=num2+=num3
print(num1)
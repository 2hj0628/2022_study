# 람다로 팩토리얼 계산
# 함수명이 없기 때문에 변수로 저장

fact=lambda x:x==0 and 1 or x*fact(x-1)

print(fact(5))
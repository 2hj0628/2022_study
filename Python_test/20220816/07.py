# shallow copy(얕은 복사)의 문제점
# 요소가 변형 객체이면 변형 객체의 특성을 그대로 가져오게 된다.
# A안에 변형 객체인 리스트로 값을 넣어두고 복사한 B에 변경하게 되면
# 똑같이 A에서도 변경이 된다.

list_A=['ABC',['DEF','GHI']]
list_B=list_A.copy()

print(list_A)
print(list_B)
print()

list_B[1][0]=['GHI']
print(list_A)
print(list_B)
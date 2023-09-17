# 내장 함수 bool()을 활용해 참과 거짓을 확인할 수 있음
# 자료형의 참과 거짓:문자열,리스트,튜플,사전,숫자(setX)
# 값이 있으면 참, 없으면 거짓
# 숫자에선 0만 거짓

# 문자열
print(bool('abcdefghi'))
print(bool(''))
print(bool(str()))
print()

# 리스트
print(bool([1,2,3]))
print(bool([]))
print()

# 튜플
print(bool((1,2,3)))
print(bool(()))
print(bool(tuple()))
print()

# 사전
print(bool({'a':1,'b':2}))
# print(type({}))
print(bool({}))
print(bool(dict()))
print()

# 숫자
print(bool(10))
print(bool(0))
print(bool(-10))
# 반복 객체 함수 - jumpyter notebook에서 실행할 것(3.9버전으로)

import collections

num=[1,2,3,4]
result=isinstance(num,collections.Iterable)    #대문자로 쓰여진건 다 클래스
print(result)

str='hello! python world!'
result=isinstance(str,collections.Iterable)
print(result)

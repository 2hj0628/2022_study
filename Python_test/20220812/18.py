# 값의 추가, 수정이 매우 용이함

# 사전에 없는 키라면 새로운 값이 추가됨
d={'a':1,'b':2}
print(d)
d['c']=3
print(d)
# 기존 사전에 있는 키에 새로운 값을 선언하면 새로운 값으로 변경됨
d['a']=10
print(d)

# 기존에 없는 키를 단순히 참조한다면 에러 발생
# print(d['d'])       #KeyError
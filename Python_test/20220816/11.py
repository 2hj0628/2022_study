# 리스트의 슬라이싱

list1=['apple','banana','dog','cat','dinosaur']

print(list1)
print(list1[:])
print(list1[::])
print()

# 'banana','dog'
print(list1[1:3])
print(list1[1:3:1])

# 'apple','dog','dinosaur'
print(list1[0:5:2])
print(list1[::2])

# 'dog','cat','dinosaur'
print(list1[2:5:1])
print(list1[2:5])
print(list1[2::1])
print(list1[2:])

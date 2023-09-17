# deep copy(깊은 복사)

import copy
list_A=['ABC',['DEF','GHI']]
list_B=copy.deepcopy(list_A)

print(list_A)
print(list_B)
print()
print(id(list_A))
print(id(list_B))

list_B[1][0]=['GHI']
print(list_A)
print(list_B)
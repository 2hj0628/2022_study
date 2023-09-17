# 동일한 변수도 다른 모듈에서 가져와 재정의 가능

import math
import test

print(math.pi)
print(test.pi)
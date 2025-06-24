import numpy as np

# 花式索引： 是深拷贝
a = np.arange(1, 13).reshape(3, 4)
print(a)

b = a[[0, 1], 0:3]
print(b)

b[0][0] = 11
print(b)
print(a)


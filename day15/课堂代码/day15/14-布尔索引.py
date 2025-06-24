"""
布尔索引
 过滤数组中满足条件的元素，可以使用布尔索引
 布尔索引也是一个数组，形状和要索引的数组形状必须相同
 布尔索引返回的是原数组的副本，属于深拷贝


布尔索引也是花式索引， 属于深拷贝
"""

import numpy as np

a = np.arange(1, 5)
print(a)
# 布尔索引： 布尔索引必须是一个数组
print(a[[True, True, False, True]])

print(a >= 3)
print(a[a >= 3])
print("-==================--")
# | 表示 或
# & 表示 和， 且
print(a[(a > 3) | (a == 3)])

print("---------------------------------")
b = np.arange(1, 13).reshape(3, 4)
print(b)
# 以下的布尔索引等价 b[[0, 2], [1, 3]]
print(b[[True, False, True], [False, True, False, True]])
print(b[[0, 2], [1, 3]])

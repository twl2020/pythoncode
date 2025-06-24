"""
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) 转为一维数组。 请使用至少三种方式实现。
"""

import numpy as np

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# 方式一
a1 = np.reshape(arr_3d, -1)
print(a1)

a2 = arr_3d.reshape(-1)
print(a2)

# 方式二
# flatten: 压平， 扁平化
# flatten(): 将多维数组压平成一维数组
a3 = arr_3d.flatten()
print(a3)

# 方式三
# ravel(): 散开, 将多维数组压平成一维数组
a4 = arr_3d.ravel()
print(a4)

# 方式四
a5 = np.array(np.nditer(arr_3d))
print(a5)

# 方式五
a6 = np.array(arr_3d.flat)
print(a6)


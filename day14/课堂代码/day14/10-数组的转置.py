"""
数组的转置需要使用： 数组的T属性
数组转置就是将数组的轴的索引倒置

一维数组不能转置
二维数组形状（n, m）转置后形状是 (m， n)

多维数组形状（a0, a1,…an-1, an）转置后形状是（ an, an-1,…a1, a0）

"""

import numpy as np

list01 = [[1, 2, 3, 4], [5, 6, 7, 8]]
a = np.array(list01)
print(a)
print(a.shape)

# 二维数组转置操作
b = a.T
print(b)
print(b.shape)  # (4, 2)

print("----------------------------------------")
list02 = [[[1, 2, 3, 4]], [[5, 6, 7, 8]], [[9, 10, 11, 12]]]
c = np.array(list02)
print(c)
print(c.shape)  # (3, 1, 4)

d = c.T
print(d)
print(d.shape)
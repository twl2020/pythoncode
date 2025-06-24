"""
如何获得两个 Python NumPy 数组中共同的项？
   问题：获取数组 a 和 b 中的共同项。
   输入：
      a = np.array([1,2,3,2,3,4,3,4,5,6])
      b = np.array([7,2,10,2,7,4,9,4,9,8])
    期望输出：[2, 4]
    提示：交集
"""

import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

c = np.intersect1d(a, b)
d = c.tolist()
print(d, type(d))

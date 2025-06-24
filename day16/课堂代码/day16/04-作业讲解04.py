"""
如何在 2d NumPy 数组中交换两个列？
问题：在数组 arr 中交换列 1 和列 2。
arr = np.arange(9).reshape(3,3)
"""

import numpy as np

arr = np.arange(9).reshape(3, 3)
arr[:, [0, 1]] = arr[:, [1, 0]]
print(arr)

"""
数组的转置需要使用： arr.transpose()

"""

import numpy as np

list02 = [
    [[1, 2, 3, 4], [11, 12, 13, 14]],
    [[5, 6, 7, 8], [15, 16, 17, 18]]
]
c = np.array(list02)
print(c)
print(c.shape)  # (2, 2, 4)

# 三维转置
d = c.transpose(0, 2, 1)
print(d.shape)
print(d)

"""
...的作用： 表示没有显式给定的轴获取全部内容

... 表示 Ellipsis

... 只能出现一次
"""

import numpy as np

a = np.arange(1, 13).reshape(2, 3, 2)
print(a)
print(a[1])  #
print(a[1, :, :])  #
# a[1, ...] 等价于 a[1, :, :]  等价于 a[1]
print(a[1, ...])  #

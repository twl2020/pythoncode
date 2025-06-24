"""
使用代码完成下面的二维数组，边界值为1，其余值为0
[[1. 1. 1. 1. 1.]
[1. 0. 0. 0. 1.]
[1. 0. 0. 0. 1.]
[1. 0. 0. 0. 1.]
[1. 1. 1. 1. 1.]]
"""

import numpy as np

# 方式一:
# 先得到一个5行5列，元素是1的二维数组
# 再将中间3行3列的区域的元素修改成0
a1 = np.ones((5, 5))
# a1[1:4, 1:4] = [0, 0, 0]
a1[1:4, 1:4] = 0
print(a1)

# 方式二:
# 先得到一个3行3列，元素是0的二维数组
# 再在外层补一圈1

b1 = np.zeros((3, 3))
# pad(): 表示填充
# pad(array, pad_width, mode='constant', **kwargs):
# pad_width: 需要填充的宽度
# mode='constant': 表示填充的模式， constant表示常量
# constant_values: 指定填充的常量值是多少
b1 = np.pad(b1, 1, mode='constant', constant_values=1)
print(b1)

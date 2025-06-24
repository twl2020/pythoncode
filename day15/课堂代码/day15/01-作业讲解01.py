"""
在不使用硬编码的前提下创建以下模式。仅使用 NumPy 函数和以下输入数组 a。
      输入a = np.array([1,2,3])
      期望输出：[1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
      提示： np.repeat() 和 np.tile() 函数
"""
import numpy as np

a = np.array([1, 2, 3])

# repeat: 将数组中的每个元素重复
b = np.repeat(a, 3)
print(a)
print(b)

# tile： 将数组整体进行重复
c = np.tile(a, 3)
print(c)

# 将b和c的结果进行拼接
# d = np.append(b, c)
# d = np.hstack((b, c))
d = np.concatenate((b, c))
print(d.tolist())




import numpy as np


a = [[[1, 2, 3, 4], [2, 3, 4, 5]], [[5, 6, 7, 8], [9, 10, "hello", True]]]

# ndarray数组中元素的形状必须一样， 数据类型也要相同
b = np.array(a)
print(b.shape)  # (2, 2, 4)
print(b.dtype)  # np.unicode_
print(b)

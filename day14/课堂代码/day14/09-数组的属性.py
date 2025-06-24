"""
ndarray.ndim：数组的轴数（维度）。
ndarray.shape：数组的形状。这是一个整数元组，指示数组每个维度的大小。对于n行m列的矩阵，shape将为(n,m)。因此，元组的长度 shape就是轴的数量ndim。
ndarray.size：数组元素的总数。这等于 shape的元素的乘积。
ndarray.dtype：描述数组中元素类型的对象。可以使用标准 Python 类型创建或指定数据类型。此外，NumPy 还提供了自己的类型。 numpy.int32、numpy.int16 和 numpy.float64 是一些示例。
ndarray.itemsize：数组中每个元素的大小（以字节为单位）。
ndarray.nbytes: 数组总字节大小（以字节为单位）。等于 size * itemsize
"""

import numpy as np

list01 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(list01)
print(arr)
print(arr.ndim)  # 2
print(arr.shape)  # (2, 4)
print(arr.size)  # 8
print(arr.dtype)  # int32
print(arr.itemsize)  # 4
print(arr.nbytes)  # 4

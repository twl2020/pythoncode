"""
您可以使用np.newaxis/None和np.expand_dims来增加现有数组的维度。
使用np.newaxis/None一次后，数组的维度就会增加一维。这意味着1D数组将变成2D数组， 2D数组将变成3D数组，依此类推。
np.newaxis 对应维度的大小是1
none 是np.newaxis的别名

np.newaxis 和 reshape的区别：
  reshape可以改变形状， 也就意味着可以升维，降维
  np.newaxis用于升维， 维度的大小是1, 但是可以配合切片使用， 升维后的数组元素数量可以和原数组的数量不同

数组的升维， 后面会使用到， 大家多加练习
"""

import numpy as np

a = np.arange(1, 13)
print(a)
print(a.shape)  # (12, )

# 将以上的一维数组升维为二维数组
b = a[:, np.newaxis]
print(b)
print(b.shape)  # (12, 1)

print("--------------------------")
b = a[np.newaxis, :6]
print(b)
print(b.shape)  # (1, 6)

print("--------------------------")
# b = a[np.newaxis, :6, np.newaxis]
b = a[None, :6, None]
print(b)
print(b.shape)  # (1, 6, 1)

print("--------------------------")
c = np.expand_dims(a, axis=0)
print(c)
print(c.shape)  # (1, 12)

print("--------------------------")
# 因为a是一维的， 所以使用expand_dims只能升二维， 也就是axis只能是0或1

c = np.expand_dims(a, axis=1)
# axis=-1  表示的是索引最大的轴
# 升维为二维， 索引最大的轴是1， 所以axis=-1 等价于 axis=1
# c = np.expand_dims(a, axis=-1)
print(c)
print(c.shape)  # (12, 1)

print("--------------------------")
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
print(arr.shape)  # (3, 4)

x = np.expand_dims(arr, axis=0)
print(x)
print(x.shape)  # (1, 3, 4)

x = np.expand_dims(arr, axis=1)
print(x)
print(x.shape)  # (3, 1, 4)

x = np.expand_dims(arr, axis=2)
print(x)
print(x.shape)  # (3, 4, 1)

# -1表示最大轴的索引， 也就是轴索引中最右边的索引
x = np.expand_dims(arr, axis=-1)
# -2是轴索引中最右边的倒数第二个索引
# x = np.expand_dims(arr, axis=-2)
print(x)
print(x.shape)  # (3, 4, 1)

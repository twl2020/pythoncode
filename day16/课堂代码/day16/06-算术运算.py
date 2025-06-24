"""
乘积运算*符在 NumPy 数组中按元素进行运算，不是矩阵乘法！！

某些操作（例如+=和*=）会就地修改现有数组，而不是创建新数组。


numpy中算术运算除了使用运算符操作外， 还提供了对应的函数
"""

import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(1, 7).reshape(2, 3)
print(a)
print(a * b)
a *= b
print(a)

print("------------------------------")
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(1, 7).reshape(2, 3)
# 加法
# c = np.add(a, b)
# 减法
# c = np.subtract(a, b)
# 乘法
# c = np.multiply(a, b)
# 除法
# c = np.divide(a, b)
# 地板除， 整除
# c = np.floor_divide(a, b)
# 幂次方
c = np.power(a, b)
print(c)
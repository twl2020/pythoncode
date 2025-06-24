"""
将 Python的列表和元组转换为 NumPy 数组
Set集合转成ndarry后， 维度为0， 0维数组就不是数组， 没有意义
"""
import numpy as np

list01 = [1, 2, 3, 4, 5]
a = np.array(list01)
print(list01)
print(type(a))
print(a)
print(a.ndim)

print("--------------------------")
t1 = (1, 2, 3, 4, 5)
b = np.array(t1)
print(b)
print(b.ndim)

print("--------------------------")
set01 = {1, 2, 3, 4, 5}
c = np.array(set01)
print(type(c))  # <class 'numpy.ndarray'>
print(c)
print(c.ndim)  # 0维

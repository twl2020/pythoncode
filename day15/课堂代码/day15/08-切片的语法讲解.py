"""
切片的语法讲解：
 [start:stop] 或者 [start:stop:step]

"""

import numpy as np

a = np.arange(1, 13)
# 一维数组的切片
print(a)
print(a[1:5])  # [2 3 4 5]
print(a[1:])  # [ 2  3  4  5  6  7  8  9 10 11 12]
print(a[:5])  # [1 2 3 4 5]
print(a[:])  # [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(a[1:5:2])  # [2  4]
print(a[1::2])  # [ 2  4  6  8 10 12]
print(a[:5:2])  # [1 3 5]
print(a[::2])  # [ 1  3  5  7  9 11]
print(a[::])  # [ 1  2  3  4  5  6  7  8  9 10 11 12]

print(a[-1:-6])  # []
print(a[-6:-1])  # [ 7  8  9 10 11]
print(a[-1:-6:-1])  # [12 11 10  9  8]
print(a[::-1])  # [12 11 10  9  8  7  6  5  4  3  2  1]

print("-------------------------------------------")
a = np.arange(1, 13).reshape(3, 4)
print(a)
i = 1
print(a[i:, :])

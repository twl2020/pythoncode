"""
考虑将一维序列中的每个元素与相同长度的另一个序列中的相应元素相乘的情况。
"""

# python列表实现
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
c = []
for i, _ in enumerate(a):
    c.append(a[i] * b[i])

print(c)

print("---------------------------------")
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
c = a * b
print(c)
print(c + 3)
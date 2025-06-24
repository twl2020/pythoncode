import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
x1 = np.sum(a) / len(a)
print(x1)

x2 = a / len(a)  # 单个元素对整体数据的贡献  -- 单个元素的平均值
x3 = np.dot(x2, np.ones_like(a))
print(x3)

print(x2)
print(sum(x2))

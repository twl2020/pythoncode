"""
np.sum() 求和
np. amax() 最大值
np. amin() 最小值
np. mean() 平均值
np. average() 加权平均值
    avg = sum(a * weights) / sum(weights)

np. argmax()  最大值索引


聚合函数： 多个合成一个

聚合函数默认情况下， 按照哪一个轴进行聚合， 哪一个轴就会消失，结果就是降维了
(d1, d2, d3)  按照0轴聚合， 结果的维度是： (d2, d3)
(d1, d2, d3)  按照1轴聚合， 结果的维度是： (d1, d3)
(d1, d2, d3)  按照2轴聚合， 结果的维度是： (d1, d2)

聚合函数的结果如果想保持维度，使用参数keepdims=True
"""

import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print(a)

# x1 = np.sum(a, axis=0)
# x1 = np.sum(a, axis=1)
# x1 = np.sum(a)
x1 = np.sum(a, axis=(0, 1), keepdims=True)
print(x1)

m = np.amax(a, axis=1, keepdims=True)
print(m)

# x2 = np.mean(a, axis=0)
x2 = np.mean(a)
print(x2)

# np.average() 加权平均值
weights = np.array([[1, 2, 2, 3], [3, 2, 2, 4], [3, 4, 2, 1]])
# weights = np.ones((3, 4))
# avg = sum(a * weights) / sum(weights)
x3 = np.average(a, weights=weights)
print(x3)

# x4 = np.argmax(a)
x4 = np.argmax(a, axis=0)
print(x4)

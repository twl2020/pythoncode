"""
范数：  ----  很重要
范数： 一种衡量向量或矩阵的长度、大小或距离的方法。


向量1范数：就是向量元素的绝对值之和  曼哈顿距离
向量2范数：就是向量元素的平方和开方  欧几里得距离  欧式距离
向量无穷范数：就是向量元素的最大值

我们后面使用比较多的就是欧式距离
欧式距离可以用来计算相似度

fro: Frobenius
"""

import numpy as np

a = np.array([1, 4, 5, 7, 3])
b = np.array([1, 4, 15, 17, 6])
c = np.array([1, 4, 7, 9, 2])

# 计算向量之间的相似度，所以可以使用欧式距离： 2范数
# 计算ac向量的2范数
n1 = np.linalg.norm((c - a), ord=2)
print(n1)
# 计算ab向量的2范数
n1 = np.linalg.norm((b - a), ord=2)
print(n1)

# 无穷范数
x = np.linalg.norm(a, ord=np.inf)
print(x)




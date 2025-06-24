"""
乘积运算 * 符在 NumPy 数组中按元素进行运算。
矩阵乘积可以使用@运算符（在 python >=3.5 中）或dot函数或方法来执行。

向量的点乘： 逐元素相乘再相加
 [a1, a2, a3] @ [b1, b2, b3]  = a1b1 + a2b2 + a3b3

矩阵的点乘：
    必须满足的形状要求是：(m, n) @ (n, k)
    结果的形状是（m, k
    也就是第一个矩阵1轴的长度必须和第二个矩阵0轴的长度相同
"""
import numpy as np

np.random.seed(0)
a = np.arange(1, 6)
b = np.random.randint(1, 10, size=(5,))
print(a)
print(b)

# * 表示逐元素相乘
print(a * b)
print("=================================")
print(a @ b)
print(np.dot(a, b))
print(a.dot(b))

print("=================================")
m = np.arange(1, 13).reshape(3, 4)
n = np.random.randint(1, 13, size=(4, 5))
print(m)
print(n)
print(m @ n)
print(np.dot(m, n))
print(m.dot(n))

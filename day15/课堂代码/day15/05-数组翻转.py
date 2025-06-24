"""
NumPy 的np.flip()函数允许您沿轴翻转或反转数组的内容。
使用 时np.flip()，指定要反转的数组和轴。
如果您不指定轴，NumPy 将沿输入数组的所有轴反转内容。

"""
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print(a)

print("-------------------------------")
# 翻转
# b = np.flip(a, 1)
# 所有轴都翻转
b = np.flip(a)
print(b)

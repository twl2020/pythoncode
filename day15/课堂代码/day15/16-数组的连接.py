"""
连接数组使用np.concatenate()：
    concatenate((a1, a2, ...), axis=0)

"""
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([11, 12, 13, 14])
c = np.concatenate((a, b))
print(c)

print("---------------------------------")
x = np.arange(1, 13).reshape(3, 4)
y = np.arange(11, 23).reshape(3, 4)
print(x)
print(y)
# z = np.concatenate((x, y))
z = np.concatenate((x, y), axis=1)
print(z)

print("---------------------------------")
m = np.array([[1, 2], [3, 4]])
n = np.array([[5, 6]])
# concatenate(): 要求对应轴必须能够匹配
k = np.concatenate((m, n.T), axis=1)
print(m)
print(n)
print(k)

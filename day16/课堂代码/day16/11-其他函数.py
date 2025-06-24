"""
np.append() 追加
np.delete() 删除
np.squeeze(a, axis=None)：从' a '移除长度为1的轴。
np.unique() 去重， 并按照从小到大的顺序排序
np.where() 相当于三目运算符
"""
import numpy as np

np.random.seed(0)
a = np.arange(1, 7).reshape(2, 3)
b = np.random.randint(3, 10, size=6).reshape(2, 3)
print(a)
print(b)

# 多维数组没有指定轴， 就会变成一维进行追加元素
# c = np.append(a, b)
c = np.append(a, b, axis=1)
print(c)

# np.delete() 删除
# obj 传入的是索引
# 多维数组没有指定轴， 就会变成一维进行追加元素
# d = np.delete(a, 2)
d = np.delete(a, 1, axis=0)
print(d)

print("-------------------------------------------")
# np.squeeze(a, axis=None)：从' a '移除长度为1的轴。
a = np.arange(1, 7).reshape(1, 2, 3, 1)
print(a)
k = np.squeeze(a)
print(k)

# np.unique() 去重， 并按照从小到大的顺序排序
a = np.array([1, 5, 2, 4, 7, 3, 4, 2, 4, 3, 6, 3])
b = np.unique(a, return_counts=True)
print(a)
print(b)

print("---------------------------------------")
# np.where() 相当于三目运算符
a = np.array([1, 5, 2, 4, 7, 3, 4, 2, 4, 3, 6, 3])
b = np.where(a == 3, 33, a)
print(b)

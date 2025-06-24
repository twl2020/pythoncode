import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print(a)

# 多维数组的迭代是相对于第一个轴完成的。
for i in a:
    print(i)

print("-------------------------")
# 如果想要对数组中的每个元素执行操作，可以使用迭代器：
for i in np.nditer(a):
    print(i)

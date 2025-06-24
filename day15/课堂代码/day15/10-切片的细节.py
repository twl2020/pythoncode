import numpy as np
"""
细节点： 
   1. 切片操作返回一个新的数组
   2. 修改新数组的元素会影响原数组  （因为是浅拷贝）
"""
a = np.arange(1, 12)
print(a)
b = a[1:6]
print(b)  # [2 3 4 5 6]

b[0] = 22
print(b)  # [22  3  4  5  6]
print(a)  # [ 1 22  3  4  5  6  7  8  9 10 11]

"""
np.zeros(shape，dtype): 返回一个给定形状和类型，元素全部是0的新数组
 - shape: 表示数组的形状，  值是： int or tuple of ints
np.ones(shape，dtype): 返回一个给定形状和类型，元素全部是1的新数组
np.full(shape, fill_value, dtype): 返回一个给定形状和类型，元素用' fill_value '填充的新数组
np.empty(shape): 返回指定形状的数据类型的数组， 元素是没有初始化的， 是随机获取的内存中的垃圾值

np.zeros_like(arr): 返回一个形状，数据类型和arr相同，但是元素是0的数组


"""

import numpy as np

# arr01 = np.zeros(3)  # 得到一维数组， 元素是3个0
# arr01 = np.zeros((3,))  # 得到一维数组， 元素是3个0
# arr01 = np.zeros((3, 2))  # 得到二维数组， 3行2列的二维数组

# 得到三维数组, 三维数组中有3个二维数组，每个数组都是2行4列
# （每个二维；里面有2个1维；每个1维中有4个元素）
arr01 = np.zeros((3, 2, 4))
print(arr01)
print(arr01.shape)

print("------------------------------------------")
arr02 = np.ones((2, 4), dtype="f4")
print(arr02)
print(arr02.shape)

print("------------------------------------------")
arr03 = np.full((3, 4, 2), fill_value=10)
print(arr03)
print(arr03.shape)

print("------------------------------------------")
arr04 = np.empty((3, 4))
print(arr04)
print(arr04.shape)

print("------------------------------------------")
list01 = [[1, 2, 3], [4, 5, 6]]
arr05 = np.array(list01, dtype="f4")
print(arr05)
print(arr05.shape)

# 返回一个形状，数据类型和arr相同，但是元素是0的数组
arr06 = np.zeros_like(arr05)
print(arr06)

print("------------------------------------------")
list02 = [[1, 2, 3], [4, 5, 6]]
# 直接创建元素数据类型是float32的数组
arr07 = np.float32(list02)
print(arr07)

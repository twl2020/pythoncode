"""
索引： 获取的单个值
切片： 获取的一个范围的值， 切片底层也是使用索引操作的

索引访问：
一维数组可以被索引、切片和迭代： 数组[索引]
多维数组的每个轴可以有一个索引： 数组[0轴索引][1轴索引] 或者 数组[0轴索引，1轴索引]
当提供的索引少于轴的数量时，缺少的索引被视为完整的切片


数组[0轴索引][1轴索引] 和 数组[0轴索引，1轴索引]是还有区别的：
数组[0轴索引][1轴索引]的执行是：
 1. 数组[0轴索引] 获取到一个临时的数组
 2. [1轴索引]是在临时数组中获取通过  临时数组[1轴索引]  获取元素的

数组[0轴索引，1轴索引] 直接在原数组的对应轴定位元素， 不会产生临时数组。
"""
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print(a)
print(a[0][2])  # 3
print(a[0])  # [ 1  2  3  4]
print(a[0][2])  # 3

print("-----------------------------")
print(a[0, 2])  # 3

print("===================================")
print(a)
x = a[1:3][1:3]
print(x)  # [[ 9 10 11 12]]

y = a[1:3, 1:3]
"""
[[ 6  7]
 [10 11]]
"""
print(y)

print("---------------------------------")
# 当提供的索引少于轴的数量时，缺少的索引被视为完整的切片
print(a)
print(a[1])

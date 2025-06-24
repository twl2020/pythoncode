"""
Series是一维的数组型对象，能够保存任何数据类型(int，str, float，python object)，
包含了数据标签，称为索引

Series由数据和索引组成
    索引(index)在左， 数据(values)在右
    索引是自动创建的

Series和DataFrame中存在两种索引:
  1. 位置索引： 自动生成的， 用数字来表示， 从0开始
  2. 标签索引： 人为设置的， 没有人为设置标签索引， 标签索引使用的就是位置索引
"""
import numpy as np
import pandas as pd

# 方式一：使用列表创建Series
# list01 = [1, 4, 6, 2, 7, 3]
# 方式二：使用元组创建Series
# list01 = (1, 4, 6, 2, 7, 3)
# 方式三：使用ndarray创建Series
list01 = np.array((1, 4, 6, 2, 7, 3))
# data 接收传入的数据
# index: 设置的标签索引
# dtype: 表示元素的数据类型， 直接使用numpy数据类型或者python数据类型
# name: 当前Series的名称
# s1 = pd.Series(data=list01, index=["a", "b", "c", "d", "e", "f"])
s1 = pd.Series(data=list01, index=[*"abcdef"], dtype="i4", name="分数")
print(s1)
# print(s1[2])

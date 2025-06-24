"""
通过索引获取数据
    位置索引： series[数字] 或者 series[[数字1， 数字n]]
    标签索引： series[标签名] 或者 series[[标签名1, 标签名n]

注意：
series[[数字1， 数字n]] 或 series[[标签名1, 标签名n] 得到的还是一个Series

"""

import pandas as pd

data = [11, 12, 13, 14, 15]
s1 = pd.Series(data, index=[*"abcde"])
print(s1)

# s1[索引]: 优先使用的是标签索引
# s1[位置索引]： 已经过时了， 推荐使用iloc
print(s1[0])
print("--------------------------")
print(s1[[0, 3]])
print("=============================")
print(s1["a"])
print(s1[["a", "e"]])

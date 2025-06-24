"""
通过切片获取数据
    位置切片：前闭后开
    [start:stop:step]

    标签切片： 前闭后闭
    [start:stop:step]

"""
import pandas as pd

data = [11, 12, 13, 14, 15, 16, 17, 18]
s1 = pd.Series(data, index=[*"abcdefgh"])
print(s1)

# 位置索引的切片操作 -- 前闭后开
# print(s1[0:5])
# print(s1[5:0:-1])
# print(s1[:5])
# print(s1[2:])


print("--------------------------------")
# 标签索引的切片操作 -- 前闭后闭
# print(s1["a":"c"])
# print(s1["c":"a":-1])
# print(s1[:"d"])
print(s1[:])
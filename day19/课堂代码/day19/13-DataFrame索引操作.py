"""
df[“列标签”] – 按照列索引获取数据
loc - 先行后列，需要通过标签索引进行获取
iloc - 先行后列，通过位置索引进行获取

先行后列： loc[0轴索引， 1轴索引]
"""
import numpy as np
import pandas as pd

data01 = np.arange(1, 13).reshape(3, 4)
df01 = pd.DataFrame(data01, columns=[*"abcd"])
print(df01)
print(df01["a"])
print("-----------------------------------")
# 以下只给了0轴的索引, 1轴就是获取所有元素
# print(df01.loc[2])
# print(df01.loc[0, "c"])
print(df01.iloc[0, 2])
"""
丢弃缺失值： dropna()
填充缺失数据：fillna()
删除行重复数据：df.drop_duplicates()
"""
import numpy as np
import pandas as pd
df01 = pd.DataFrame([1, 3, 9, np.nan, 5, np.nan, 11])
print(df01)
df02 = df01.dropna()
print(df02)


print("---------------------------------------")
df03 = df01.fillna("99")
print(df03)

print("---------------------------------------")
data = [
    [1, 3, 5, 7],
    [1, 4, 5, 7],
    [4, 3, 2, 6],
]
df04 = pd.DataFrame(data)
print(df04)
print("==========================")
# 以下的方式要求： 每一行的数据全部相同才能删除
# df05 = df04.drop_duplicates()
# subset: 用来判断删除重复数据的时候比较的是哪些列的值
# subset=[列索引]
# keep：表示删除重复数据的时候， 保留什么数据
# keep="first" 表示保留重复数据的第一行数据
# keep="last" 表示保留重复数据的最后一行数据
# keep=False 表示不保留重复数据
df05 = df04.drop_duplicates(subset=[2, 3], keep=False)
print(df05)


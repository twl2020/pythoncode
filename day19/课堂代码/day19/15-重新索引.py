"""
重新索引：会返回一个新的对象
    Series对象.reindex()
    DataFrame对象.reindex()
    DataFrame对象.reindex(columns=…)

"""
import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)
s2 = s1.reindex(index=[1, 2, 3, 6])
print(s2)

print("-----------------------------------")
data = np.arange(1, 13).reshape(3, 4)
df01 = pd.DataFrame(data, columns=[*"abcd"])
print(df01)
# labels设置的是行或者列的索引名称， 配合axis一起使用
# df02 = df01.reindex(labels=[*"xyz"], axis=1)
# fill_value的作用是填充缺失值的
df02 = df01.reindex(index=[*"xyz"], fill_value=999)
# df02 = df01.reindex(columns=[*"abc"])
print(df02)

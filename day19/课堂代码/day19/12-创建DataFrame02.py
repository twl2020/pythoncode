"""
列表构造DataFrame
    二维ndarray构造DataFrame
    字典构成的列表构造DataFrame
    Series构成的列表构造DataFrame

以上创建DataFrame的方式， 是将二维列表中的每一条数据当作DataFrame中的一行数据。
其实本质上和numpy的二维数组形式没有区别。
"""

import numpy as np
import pandas as pd

data01 = np.arange(1, 13).reshape(3, 4)
print(data01)

df01 = pd.DataFrame(data01, index=[*"abc"])
print(df01)

print("---------------------------------")

data02 = [
    {
        "id": 1001,
        "name": "李四",
        "age": 20
    },
    {
        "id": 1002,
        "name": "韩梅梅",
        "age": 24
    }
]

df02 = pd.DataFrame(data02)
print(df02)

print("---------------------------------")
data03 = [
    pd.Series([1, 2, 3, 4, 5]),
    pd.Series([11, 12, 13, 14, 15])
]
df03 = pd.DataFrame(data03)
print(df03)

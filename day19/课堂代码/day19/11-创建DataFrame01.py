"""
字典构造DataFrame
    数组、列表、元组构成的字典构造DataFrame
    Series构成的字典构造DataFrame
    字典构成的字典构造DataFrame

以上的创建方式中， 优先使用key作为列索引的名称， 其次才是行索引的名称
"""
import numpy as np
import pandas as pd

d = {
    "aa": np.array([1, 2, 3, 4, 5]),
    "bb": [11, 12, 13, 14, 15],
    "cc": (111, 112, 113, 114, 115),
    "dd": pd.Series((1111, 1112, 1113, 1114, 1115))
}

# 自动的将字典的key作为列索引名称
df01 = pd.DataFrame(d)
print(df01)

print("------------------------------------------")
# 字典构成的字典构造DataFrame
d1 = {
    "stu01": {
        "id": 1001,
        "name": "张三",
        "age": 23
    },
    "stu02": {
        "id": 1002,
        "name": "李四",
        "age": 22
    }
}

df02 = pd.DataFrame(d1)
print(df02)

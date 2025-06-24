"""
s.loc(标签索引 / 切片 / 函数): 根据给定的标签索引或布尔索引获取元素

s.iloc(位置索引 / 切片)：根据给定的位置索引或布尔索引获取元素
 这里的i表示的是整数位置索引， i = integer

"""

import pandas as pd

data = [11, 12, 13, 14, 15]
s1 = pd.Series(data, index=[*"abcde"])
print(s1)

# x = s1.loc["a"]
# x = s1.loc["a":"c"]
# x = s1.loc[[True, False, True, True, True]]
# x = s1.loc[s1 > 12]
x = s1.loc[lambda e: e > 12]
print(x)

print("-------------------------------------")
# y = s1.iloc[0]
# y = s1.iloc[0:3]
y = s1.iloc[[True, True, False, False, False]]
print(y)

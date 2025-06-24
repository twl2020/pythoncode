import pandas as pd

data = [11, 12, 13, 14, 15]
s1 = pd.Series(data, index=[*"abcde"])
print(s1)
# 这里就是给Series设置名称
s1.name = "随便写的数字"
print(s1)
print("-------------------------------")
# 以下是给索引设置名称的
s1.index.name = "id"
print(s1)
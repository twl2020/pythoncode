"""
head(): 默认获取前5个元素
tail(): 默认获取后5个元素
"""

import pandas as pd

data = [11, 12, 13, 14, 15, 16, 17]
s1 = pd.Series(data, index=[*"abcdefg"])
print(s1)
print(s1.head(3))
print(s1.tail(3))
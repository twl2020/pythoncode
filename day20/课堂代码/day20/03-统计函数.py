"""
sum(): 总和。
cumsum(): 累计总和。
mean(): 平均值。
max() 和 idxmax(): 分别找出最大值及其索引位置。
min() 和 idxmin(): 分别找出最小值及其索引位置。
describe(): 提供一个包含计数、平均值、标准差、最小值、四分位数和最大值的统计摘要。
"""
import numpy as np
import pandas as pd

data = np.arange(1, 7).reshape(2, 3)
df01 = pd.DataFrame(data)
print(df01)

s = df01.sum()
print(s)

# 累计求和： ---- 下来自己演示
m = df01.mean()
print(m)

# max01 = df01.max()
max01 = df01.idxmax()
print(max01)

print("---------------------------------")
desc = df01.describe()
print(desc)

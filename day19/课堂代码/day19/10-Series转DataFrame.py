import numpy as np
import pandas as pd

"""
Series转DataFrame:
 1. 方式一： DataFrame()
 2. 方式二： series的to_frame()方法


"""
data = np.arange(10, 16)
s1 = pd.Series(data, index=[*"abcdef"], name="info")
print(s1)
print("------------------------------")
# Series转DataFrame的时候， index的值如果是Series的标签索引，就会获取对应的值；否则就是NaN
# columns设置的就是列索引:
# 1. 如果Series设置了name, 此时没有显式的指定columns， 列索引的名称就是Series的name
# 2. 如果Series没有设置了name, 此时没有显式的指定columns， 列索引的名称就是从0开始的值
# 3. 显式的指定columns， 列索引的名称就是指定的值
df01 = pd.DataFrame(s1, index=[*"abcdef"], columns=["xxx", "info"])
print(df01)

print("=============================")
# to_frame(name): 将Series转成DataFrame, name的值会替换Series的name
df02 = s1.to_frame("yyy")
print(df02)
"""
_append: 只有Series才有才该函数
insert(): Series和DataFrame都有该函数
drop(): Series和DataFrame都有该函数
"""
import numpy as np
import pandas as pd

data = np.arange(1, 13).reshape(3, 4)
df01 = pd.DataFrame(data)
print(df01)

s1 = df01[0]
print(s1)
s2 = s1._append(df01[1])
print(s2)

print("---------------------------------------------")
# loc: 表示插入的列索引位置
# column： 列标签的名称
# value: 插入的值, 可以是标量或数组
df01.insert(2, 5, np.array([100, 99, 98]))
print(df01)

print("---------------------------------------------")
df01.drop(labels=5, axis=1, inplace=True)
print(df01)
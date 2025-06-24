"""
T转置
通过列索引获取列数据（Series类型）
增加列数据
删除列
"""

import numpy as np
import pandas as pd

data01 = np.arange(1, 13).reshape(3, 4)
df01 = pd.DataFrame(data01)
print(df01)
# T转置
df02 = df01.T
print(df02)
# 通过列索引获取列数据（Series类型）
print(df01[0])
# 增加列数据
df01["a"] = [100, 99, 98]
print(df01)

# 删除列
del df01["a"]
# del(df01["a"])
print(df01)
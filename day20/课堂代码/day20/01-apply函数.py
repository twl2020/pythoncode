import numpy as np
import pandas as pd

data = np.arange(10, 16)
df01 = pd.DataFrame(data)
print(df01)
print("---------------------------------------")
df02 = df01.apply(lambda s: np.sum(s))
print(df02)
print("---------------------------------------")
df03 = df01.apply(np.sum)
print(df03)
print("---------------------------------------")
# sum是python内置的函数
df04 = df01.apply(sum)
print(df04)
print("---------------------------------------")
# "sum" 是DataFrame对象的函数
df05 = df01.apply("sum")
print(df05)
print("---------------------------------------")
df06 = df01.apply([np.sum, np.mean])
print(df06)
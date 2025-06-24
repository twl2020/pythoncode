"""
算术运算:
   x.add(y) ===> x + y
   x.radd(y) ===> y + x
"""
import numpy as np
import pandas as pd

data = np.arange(1, 13).reshape(3, 4)
df01 = pd.DataFrame(data)
print(df01)

# 加法运算
print(df01.add(3))
print("-------------------------")
print(df01.radd(3))
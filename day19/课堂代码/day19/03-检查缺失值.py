"""
NaN: 表示缺失值

isnull和notnull 检查缺失值

"""
import numpy as np
import pandas as pd

data = np.array([1, 2, np.NAN, 4, np.nan, 5, np.NaN])
s1 = pd.Series(data)
# isnull: 返回的是元素是bool类型的Series, 如果是NaN， 对应就是True
s2 = s1.isnull()
# notnull: 返回的是元素是bool类型的Series, 如果不是NaN， 对应就是True
s3 = s1.notnull()
print(s1)
print(s2)
print(s3)

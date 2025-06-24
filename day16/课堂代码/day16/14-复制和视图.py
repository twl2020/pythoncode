"""
复制和视图

复制： copy() -- 深拷贝
视图： view() -- 浅拷贝
"""

import numpy as np

a = np.arange(1, 13).reshape(2, 3, 2)
print(a)

# b = a.copy()
b = a.view()
b[0][0][0] = 100
print(b)
print(a)
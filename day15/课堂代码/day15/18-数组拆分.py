"""
np.split(ary, indices_or_sections, axis=0)
np.hsplit(ary, indices_or_sections): 将原数组按照1轴平均拆分成多个子数组
np.vsplit(ary, indices_or_sections)

"""

import numpy as np

a = np.arange(1, 13).reshape(3, 4)
print(a)
# b = np.hsplit(a, 2)
# [1, 2] 表示的是  [:1] [1:2] [2:]
b = np.split(a, [1, 2], axis=1)
print(b)
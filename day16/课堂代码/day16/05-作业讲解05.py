"""
 如现在四位同学对球球、冷檬、蘑菇头、松韵 三种舞蹈进行打分的一个数据（总分为10），每个
同学分别从2个维度统计分数：
1. 计算每一种舞蹈的评分总和
2. 计算每位同学的评分总和
"""

import numpy as np

item = np.array([
    [3, 5, 8],
    [4, 6, 5],
    [3, 8, 3],
    [2, 6, 9]
])

# 1. 计算每一种舞蹈的评分总和
dance_score01 = np.sum(item, axis=0)
print(dance_score01)

# 2. 计算每位同学的评分总和
dance_score02 = np.sum(item, axis=1)
print(dance_score02)



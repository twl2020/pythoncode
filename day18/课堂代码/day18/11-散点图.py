"""
散点图（Scatter plot）是数据可视化中一种常见的图表类型，
用于显示两个变量之间的关系。它通常用于观察数据的分布情况和检测变量之间的相关性。
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 300, 200, 180, 400])
y = np.array([60, 200, 100, 180, 300])

plt.scatter(x, y, c="r", marker="*")
# 设置网格
plt.grid()
# 保存图片
plt.savefig("scatter.png")

plt.show()





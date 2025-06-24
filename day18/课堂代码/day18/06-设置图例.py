"""
设置图例

当axes上绘制和多个图形的时候，可以使用图例来区分图形

图例的位置是自动设置的， 会自动的选择一个尽量不遮挡图形的地方显示
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi * 2, np.pi * 2)

# 设置图例的方式一： 当绘图的时候没有设置label标签的时候使用
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.legend(["sin", "cos"])

# 设置图例的方式二： 当绘图的时候设置label标签的时候使用
plt.plot(x, np.sin(x), label="sin")
plt.plot(x, np.cos(x), label="cos")
plt.legend()
plt.show()

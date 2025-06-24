"""
柱状图是一种用矩形柱来表示数据分类的图标，可以垂直绘制，也可以水平绘制，它的高度和所表示的数值成正比关系。
plt.bar()
plt.barh()  ： 条形图

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 300, 200, 180, 400])
# plt.bar(x, x, width=10)
plt.barh(x, x, 10)
plt.show()
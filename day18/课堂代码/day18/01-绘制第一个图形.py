"""
绘制一个正弦曲线的图形
"""
import numpy as np
import matplotlib.pyplot as plt


# 准备正弦曲线的xy坐标
x = np.linspace(0, np.pi * 2)
y = np.sin(x)

# 将以上的xy绘制通过折线图绘制出来
plt.plot(x, y)

# 为了能够看见绘制的图表， 需要将程序阻塞， 不往下执行
# show方法的作用就是显示图标， 同时程序会被阻塞
plt.show()

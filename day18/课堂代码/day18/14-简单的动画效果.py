import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 2)
# 以下的line是从list中解包得到的Line2D
line, = plt.plot(x, np.sin(x))
for i in np.arange(0, np.pi * 10, 0.1):
    # 在循环中更改折线图的y值即可
    # line.set_ydata(np.sin(x+i))
    # 设置x和y的数据
    line.set_data(x, np.sin(x + i))
    plt.pause(0.1)

plt.show()

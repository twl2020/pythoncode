import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi * 2)
list01 = plt.plot(x, np.sin(x))
for i in np.arange(0, np.pi * 10, 0.1):
    # 在循环中更改折线图的y值即可
    list01[0].set_ydata(np.sin(x+i))
    plt.pause(0.1)

plt.show()
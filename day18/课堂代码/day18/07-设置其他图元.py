import numpy as np
import matplotlib.pyplot as plt

# 图像中显示中文
plt.rcParams['font.sans-serif'] = "SimHei"

# 图片中显示符号
plt.rcParams['axes.unicode_minus'] = False

x = np.linspace(-np.pi * 2, np.pi * 2)

_, axes_list = plt.subplots(2, 2)
axes_arr01, axes_arr02 = axes_list
a1, a2 = axes_arr01
a3, a4 = axes_arr02

a1.plot(x, np.sin(x))
a1.legend(["sin"])
# 设置标题
a1.set_title("绘制的正弦曲线")
# 设置x轴的标签
a1.set_xlabel("x坐标的值")
a1.set_ylabel("y坐标的值")

a2.plot(x, -np.sin(x))
a2.legend(["-sin"])
a2.set_title("绘制的正弦曲线")

a3.plot(x, np.cos(x))
a3.legend(["cos"])
a3.set_title("绘制的cos曲线")

a4.plot(x, -np.cos(x))
a4.legend(["-cos"])
a4.set_title("绘制的cos曲线")

# 调整布局
plt.tight_layout()
plt.show()

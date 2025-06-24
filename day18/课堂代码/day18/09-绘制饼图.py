"""
饼状图用来显示一个数据系列中各项数据占项目数据总和的百分比
plt.pie()

"""
import numpy as np
import matplotlib.pyplot as plt

# 图像中显示中文
plt.rcParams['font.sans-serif'] = "SimHei"

# 图片中显示符号
plt.rcParams['axes.unicode_minus'] = False

x = np.array([100, 200, 130, 90])
plt.pie(x,
        labels=["苹果", "香蕉", "梨子", "草莓"],
        autopct="%.2f%%",
        shadow=True,
        explode=[0, 0, 0.1, 0])

plt.show()

"""
sigmoid函数： （S型生长曲线）
1. 公式必须记住： 1 / (1 + e ** -x)
2. 曲线图必须记住
3. 值域范围： (0, 1), 有饱和区间
4. 用在深度学习模型的输出层， 用来解决二分类问题
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
# sigmoid函数
# y = 1 / (1 + np.e ** -x)
y = 1 / (1 + np.exp(-x))

# sigmoid的导数
dy = y * (1 - y)
plt.plot(x, y)
plt.plot(x, dy, color="red")
plt.grid(True)
plt.show()
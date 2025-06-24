"""
relu函数： 线性整流函数
1. 公式必须记住： max(x, 0)
2. 曲线图必须记住
3，值域： [0, +∞)
4. 使用场景：用在深度学习模型的中间层， 将线性变成非线性
"""
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10)
y = np.maximum(x, 0)
plt.plot(x, y)
plt.show()
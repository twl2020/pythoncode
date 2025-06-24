"""
softmax函数： 归一化指数函数
1. 公式必须记住
2. 曲线图必须记住
3. 值域：[0.0, 1.0]
4. 用在深度学习模型的输出层， 用作多分类， 结果多分类的概率值
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10)
# softmax函数
y = np.exp(x) / sum(np.exp(x))
plt.plot(x, y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2)

# 幂函数
y1 = x ** 2

# 指数函数
y2 = 2 ** x

plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="red")
plt.grid(True)
plt.show()

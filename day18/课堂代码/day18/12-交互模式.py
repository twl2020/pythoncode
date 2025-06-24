import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 300, 200, 180, 400])
y = np.array([60, 200, 100, 180, 300])

# 开启交互模式  -- pycharm使用这个没有意义， 需要python交互窗口中使用
plt.ion()

plt.scatter(x, y, c="r", marker="*")

# 关闭交互模式
plt.ioff()

# 开启交互模式，即使在脚本中遇到plt.show( )，代码还是会继续执行。
plt.show()

print("over-------------------")

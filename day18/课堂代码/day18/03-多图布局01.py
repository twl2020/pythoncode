"""
plt.subplot(nrows, ncols, index)
"""
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, np.pi * 2)

a1 = plt.subplot(2, 2, 1)
a2 = plt.subplot(2, 2, 2)
a3 = plt.subplot(2, 2, 3)
a4 = plt.subplot(2, 2, 4)

a1.plot(x, np.sin(x), "r--")
a2.plot(x, np.cos(x))
a3.plot(x, -np.sin(x))
a4.plot(x, np.tan(x))

plt.show()

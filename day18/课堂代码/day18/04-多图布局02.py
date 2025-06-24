"""
plt.subplots(nrows, ncols) -> 'tuple[Figure, Any]：
Create a figure and a set of subplots.

"""
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, np.pi * 2)

_, axes_list = plt.subplots(2, 2)
axes_arr01, axes_arr02 = axes_list
a1, a2 = axes_arr01
a3, a4 = axes_arr02

a1.plot(x, np.sin(x), "b--")
a2.plot(x, np.cos(x))
a3.plot(x, -np.sin(x))
a4.plot(x, np.tan(x))

plt.show()

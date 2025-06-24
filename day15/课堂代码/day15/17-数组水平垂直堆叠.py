"""
数组水平垂直堆叠:
  水平堆叠使用hstack， 相当于concatenate函数 axis=1
  垂直堆叠使用vstack， 相当于concatenate函数 axis=0

"""
import numpy as np

m = np.array([[1, 2], [3, 4]])
n = np.array([[5, 6]])
k = np.hstack((m, n.T))
k2 = np.vstack((m, n))
print(m)
print(n)
print(k)
print(k2)

print("--------------------------")
# stack() 可以指定轴， 后面用到的时候再讲解
# np.stack() ??
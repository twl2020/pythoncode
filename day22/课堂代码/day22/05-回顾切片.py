import numpy as np

data = np.zeros((2, 3, 3), "u1")
print(data)
# data[:] = [10, 11, 12]
data[0, :, :] = 10
print(data)

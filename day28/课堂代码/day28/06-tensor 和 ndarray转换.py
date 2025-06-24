"""
tensor 和 numpy.ndarray() 转换
"""
import numpy as np
import torch

a = np.array([1, 2, 3, 4, 5])
# 使用Tensor()构造函数将ndarray转成tensor, 但是数据类型是float32
# t1 = torch.Tensor(a)
# from_numpy() 将ndarray转成tensor
t1 = torch.from_numpy(a)
print(t1)


# tensor转ndarray
t2 = torch.tensor([1, 2, 3, 4, 5])
# tensor对象.numpy()：  tensor转ndarray
arr = t2.numpy()
print(arr)
print(type(arr))

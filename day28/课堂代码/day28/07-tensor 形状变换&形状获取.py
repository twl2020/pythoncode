"""
tensor 形状变换&形状获取
"""
import torch
# t1 = torch.arange(1, 11)
# rand()返回的是随机数， 范围在[0, 1)
t1 = torch.rand((5, 2))
print(t1)
# 修改形状
# t2 = torch.reshape(t1, (2, 5))
# t2 = t1.reshape((2, 5))
t2 = t1.view((2, 5))
print(t1)
print(t2)
# 获取tensor的形状
print(t2.shape, t2.shape[0])
# 获取tensor的形状
print(t2.size(), t2.size()[0], t2.size(0))


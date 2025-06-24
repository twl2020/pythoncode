"""
多维张量的自动微分
"""

import torch

x = torch.arange(1, 7, dtype=torch.float32, requires_grad=True)
x1 = x.reshape((2, 3))
print(x)
y = x1 ** 2

# 除了标量外， 其余的张量使用backward反向求导的时候，
# backward必须接收一个形状和叶子节点相同， 元素全部是1的tensor
x1.retain_grad()
y.backward(torch.ones_like(x1))  # y对x反向求导
print(x1.grad)

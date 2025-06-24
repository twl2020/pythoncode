"""
回归任务的损失函数有：
1. MAE损失函数： 平均绝对值损失函数; 也叫做L1损失函数
2. MSE损失函数： 均方损失函数, 也叫做L2损失函数
"""

import torch
import torch.nn as nn

y_true = torch.tensor([2.0, 3.2, 1.9])
y_pred = torch.tensor([2.1, 3.1, 1.8])

loss_fn = nn.L1Loss()
loss = loss_fn(y_pred, y_true)
print(loss)

mse = nn.MSELoss()
loss = mse(y_pred, y_true)
print(loss)


# SmoothL1Loss额外引入了一个超参数β， 默认是1.0
smooth = nn.SmoothL1Loss()
loss = smooth(y_pred, y_true)
print(loss)


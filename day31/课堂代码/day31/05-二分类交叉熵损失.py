import torch
import torch.nn as nn
from torch.nn import functional as F

# ⼆分类中每个样本的预测值只有⼀个值
logits = torch.tensor([1.70, -0.38, 2.14])

# 三个样本的类别
targets = torch.tensor([0, 1, 0], dtype=torch.float32)

# 使用BCELoss计算损失
loss_fn = nn.BCELoss()

# RuntimeError: all elements of input should be between 0 and 1
# 说明BCELoss是没有自带sigmoid
sm = F.sigmoid(logits)
loss = loss_fn(sm, targets)
print(loss)  # tensor(1.6734)

# BCEWithLogitsLoss自带sigmoid函数的
loss_fn01 = nn.BCEWithLogitsLoss()
loss01 = loss_fn01(logits, targets)
print(loss01)  # tensor(1.6734)

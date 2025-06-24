import torch
from torch import nn
from torch.nn import functional as F

# logits就是模拟的模型训练多分类得到的得分
# 以下数据表示的是 3个样本，每个样本5个类别对应的得分数据
# logits的形状是： (3, 5)
logits = torch.tensor([[-1.4925, -1.4033, 0.8390, -1.6440, 1.5562],
                       [2.0672, -0.3932, -1.2632, 0.6108, 1.3722],
                       [-1.5822, -0.0761, 0.3674, -1.7704, 0.1582]])

# targets表示的是三个样本的真实类别
# targets的形状是： (3, )
targets = torch.tensor([0, 3, 4])

# 1. NLLLoss也会将 targets 进行 one-hot
# 2. log_softmax + NLLLoss = CrossEntropyLoss
# 3. NLLLoss默认计算的是平均损失
# loss_fn = nn.NLLLoss()
loss_fn = nn.NLLLoss(reduction="sum")
# logits = F.log_softmax(logits, dim=1)
p = F.log_softmax(logits, dim=-1)
loss = loss_fn(p, targets)
print(loss)

# 手动验证
# softmax = F.softmax(logits)
# print(softmax)

b = -((1 * F.math.log(0.0291) + 0 * F.math.log(0.0318) + 0 * F.math.log(0.2998) +
       0 * F.math.log(0.0250) + 0 * F.math.log(0.6142)) +
      (0 * F.math.log(0.5396) + 0 * F.math.log(0.0461) +
       0 * F.math.log(0.0193) + 1 * F.math.log(0.1258) +
       0 * F.math.log(0.2693)) + (0 * F.math.log(0.0525) +
                                  0 * F.math.log(0.2365) +
                                  0 * F.math.log(0.3686) +
                                  0 * F.math.log(0.0435) + 1 * F.math.log(0.2990)))
print(b)
print(b / 3)

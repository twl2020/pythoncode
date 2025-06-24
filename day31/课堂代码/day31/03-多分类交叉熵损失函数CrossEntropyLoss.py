import torch
from torch import nn

# logits就是模拟的模型训练多分类得到的得分
# 以下数据表示的是 3个样本，每个样本5个类别对应的得分数据
# logits的形状是： (3, 5)
logits = torch.tensor([[-1.4925, -1.4033, 0.8390, -1.6440, 1.5562],
                       [2.0672, -0.3932, -1.2632, 0.6108, 1.3722],
                       [-1.5822, -0.0761, 0.3674, -1.7704, 0.1582]])

# targets表示的是三个样本的真实类别
# targets的形状是： (3, )
targets = torch.tensor([0, 3, 4])

# 使用CrossEntropyLoss计算损失
#  logits的形状是： (3, 5) 而 targets的形状是： (3, ), 两个的形状不一样，
#  但是计算交叉熵的时候没有报错， 为什么？
# 因为， CrossEntropyLoss损失函数帮我们完成了以下工作：
# 1. CrossEntropyLoss会将真实标签targets进行one-hot编码
#   0:   1,0,0,0,0
#   3:   0,0,0,1,0
#   4:   0,0,0,0,1
# 此时targets的形状就变成了(3, 5)
# 2. CrossEntropyLoss会将logits传给log_softmax()函数得到logits的概率, 再进行对数计算
# 3. CrossEntropyLoss默认计算的是平均损失
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(logits, targets)
print(loss)


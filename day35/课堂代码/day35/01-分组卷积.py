import torch.nn as nn
# 分组之后 如果原来是12 分成3组 每一组有4个通道，每个卷积核就是4个通道，输出通道是6，表示有个卷积核
# 没有分组时的参数量： 6 * 12 * 3 * 3
# layer3 = nn.Conv2d(12, 6, 3, groups=1)
# 分成三组后的参数量：6 * 4 * 3 * 3
layer3 = nn.Conv2d(12, 6, 3, groups=3)
print(layer3.weight.data.numel())
print(layer3.weight.shape)
print(6 * 4 * 3 * 3)

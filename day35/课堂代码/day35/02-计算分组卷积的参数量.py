"""
分组卷积的优点：
    1. 减少参数数量： 分组卷积通过将输入通道划分成多个组，使得每个组内的卷积核共享参数，
    从而有效地减少了模型的参数数量，降低了计算和存储的开销。
    2. 降低计算复杂度： 由于参数数量减少，可以在一定程度上降低计算复杂度，特别是在资源受限的环境中，
    如移动设备和嵌入式系统。

缺点：
   数据信息只存在本组里面,  通道之间的信息没有融合。
"""
import torch.nn as nn

#  6 * 6 * 3 * 3  = 324
layer1 = nn.Conv2d(6, 6, 3, 1, groups=1)
# 6 * 3 * 3 * 3 = 162
layer2 = nn.Conv2d(6, 6, 3, 1, groups=2)
# 6 * 2 * 3 * 3 = 108
layer3 = nn.Conv2d(6, 6, 3, 1, groups=3)
# 6 * 1 * 3 * 3 = 54
# 深度卷积： 分组数 = 通道数
layer4 = nn.Conv2d(6, 6, 3, 1, groups=6)  # 深度卷积DW(Depthwise Convolution)

print(layer1.weight.data.numel())  # 324
print(layer1.weight.shape)  # 6, 6, 3, 3
print(layer2.weight.data.numel())  # 162
print(layer3.weight.data.numel())  # 108
print(layer4.weight.data.numel())  # 54
print(layer4.weight.shape)  # 6, 1, 3, 3

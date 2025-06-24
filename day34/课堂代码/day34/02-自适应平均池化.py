"""
自适应平均池化层与平均池化层的区别在于：
    自适应平均池化层是允许指定输出的目标尺寸，自动计算平均池化层的大小以及移动步长。

平均池化: AvgPool2d(kernel_size, stride)
自适应平均池化层: AdaptiveAvgPool2d(output_size)
        作用： 就是无论输入的数据形状是什么， 经过自适应平均池化层后得到的都是指定的output_size

使用场景：
   我们设计的CNN模型输入的数据有尺寸要求的时候， 我们就可以在网络输入层之前使用AdaptiveAvgPool2d， 得到我们需要
   的尺寸。 比如VGG中就在全连接层前使用了AdaptiveAvgPool2d


"""

import torch.nn as nn
import torch


pool = nn.AdaptiveAvgPool2d(3)
x = torch.arange(1, 17, dtype=torch.float32).reshape(1, 1, 4, 4)
print(x)
print(x.shape)

# 将数据x交给自适应平均池化
x_ = pool(x)
print(x_)
print(x_.shape)

import torch.nn as nn


# 定义第一种残差模块
class BasicBlock(nn.Module):
    # 设置expansion为1， 用于计算最终输出特征的通道数
    expansion = 1

    # 接收输入通道数， 输出通道数， 步长， 池化
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super().__init__()
        # 定义第一个卷积层， 用3*3的卷积核进行卷积，输出通道数为out_channels，步长stride， 填充1
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        # BN层
        self.bn1 = nn.BatchNorm2d(out_channels)
        # 激活函数
        self.relu = nn.ReLU(inplace=True)

        # 定义第二个卷积层， 用3*3的卷积核进行卷积，输出通道数为out_channels，步长1， 填充1
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, bias=False)
        # BN层
        self.bn2 = nn.BatchNorm2d(out_channels)
        # 下采样
        self.downsample = downsample
        # 保存步长
        self.stride = stride

    def forward(self, x):
        # 保存输入特征图
        identity = x
        # 卷积 + BN + relu
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        # 卷积 + BN
        out = self.conv2(out)
        out = self.bn2(out)

        # 如果定义了下采样， 就使用下采样调整输入x的维度
        if self.downsample:
            identity = self.downsample(identity)

        # 将identity和out相加，然后使用relu
        out += identity
        out = self.relu(out)
        return out


# 定义第二种残差模块 Bottleneck
class Bottleneck(nn.Module):
    # 设置expansion为4， 用于计算最终输出特征图的通道
    expansion = 4

    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super().__init__()
        # 定义第一层卷积层， 使用1*1卷积，输出通道数out_channels
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, bias=False)
        # BN
        self.bn1 = nn.BatchNorm2d(out_channels)
        # 定义第二层卷积层， 使用3*3卷积，输出通道数out_channels， 步长为stride, 填充1
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        # BN
        self.bn2 = nn.BatchNorm2d(out_channels)
        # 定义第三层卷积层， 使用1*1卷积，输出通道数out_channels * 4
        self.conv3 = nn.Conv2d(out_channels, out_channels * 4, kernel_size=1, bias=False)
        # BN
        self.bn3 = nn.BatchNorm2d(out_channels * 4)
        # relu
        self.relu = nn.ReLU(True)
        # 下采样， 用于调整特征的维度
        self.downsample = downsample
        # 保存步长
        self.stride = stride

    def forward(self, x):
        # 保存输入特征图
        identity = x
        # 卷积 + BN + relu
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        # 卷积 + BN + relu
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        # 卷积 + BN
        out = self.conv3(out)
        out = self.bn3(out)

        # 如果定义了下采样， 就使用下采样调整输入x的维度
        if self.downsample:
            identity = self.downsample(identity)

        # 将identity和out相加，然后使用relu
        out += identity
        out = self.relu(out)
        return out

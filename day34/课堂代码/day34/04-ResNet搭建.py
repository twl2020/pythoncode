import torch
import torch.nn as nn
from torchinfo import summary
from resnet_block import BasicBlock, Bottleneck
from torchvision import models


class ResNet(nn.Module):

    # 接收残差块类型block, 残差块数量列表layers, 类别数
    def __init__(self, block, layers, num_classes=1000):
        super().__init__()
        # 定义第一个卷积层， 使用7*7的卷积核，通道数64， stride为2， 填充为3
        self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
        # BN
        self.bn1 = nn.BatchNorm2d(64)
        # relu
        self.relu = nn.ReLU(True)
        # 定义3*3的最大池化层， stride=2， padding=1
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        # 初始化输入通道
        self.in_channels = 64
        # 定义layer1, 通道数64, 包含layers[0]个block
        self.layer1 = self.make_layer(block, 64, layers[0])
        # 定义layer2, 通道数128, 包含layers[1]个block, 步长为2
        self.layer2 = self.make_layer(block, 128, layers[1], stride=2)
        # 定义layer3, 通道数256, 包含layers[2]个block, 步长为2
        self.layer3 = self.make_layer(block, 256, layers[2], stride=2)
        # 定义layer4, 通道数512, 包含layers[3]个block, 步长为2
        self.layer4 = self.make_layer(block, 512, layers[3], stride=2)
        # 平均池化层，输出为 channel * 1 * 1
        self.avgpool = nn.AdaptiveAvgPool2d(1)
        # 定义全连接层， 输入512 * block.expansion， 输出为num_classes
        self.fc = nn.Linear(512 * block.expansion, num_classes)

    # 根据传入的配置生成网络结构
    def make_layer(self, block, out_channels, blocks, stride=1):
        # 下采样层初始为None
        downsample = None
        # 如果步长不为1或者输入通道核输出通道不一致， 则需要对输入特征进行调整
        if stride != 1 or self.in_channels != out_channels * block.expansion:
            # 定义下采样层， 包括1*1卷据和BN
            downsample = nn.Sequential(
                nn.Conv2d(self.in_channels, out_channels * block.expansion, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels * block.expansion)
            )

        # 定义一个layers列表
        layers = []
        # 将第一个block添加到layers列表中
        layers.append(block(self.in_channels, out_channels, stride, downsample))
        # 更新in_channels为下一个基本块的输入通道数
        self.in_channels = out_channels * block.expansion
        # 添加剩余的基本块带layers中
        for i in range(1, blocks):
            layers.append(block(self.in_channels, out_channels))

        # 返回所有的block
        return nn.Sequential(*layers)

    def forward(self, x):
        # 第一部分， 7*7卷积+BN+relu+最大池化
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        # 第二部分， 4组残差模块
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)

        # 第三部分， 自适应平均池化 + 全连接
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x


# 封装函数
def resnet18(num_classes=1000):
    return ResNet(BasicBlock, [2, 2, 2, 2], num_classes=num_classes)


def resnet34(num_classes=1000):
    return ResNet(BasicBlock, [3, 4, 6, 3], num_classes=num_classes)


def resnet50(num_classes=1000):
    return ResNet(Bottleneck, [3, 4, 6, 3], num_classes=num_classes)


def resnet101(num_classes=1000):
    return ResNet(Bottleneck, [3, 4, 23, 3], num_classes=num_classes)


def resnet152(num_classes=1000):
    return ResNet(Bottleneck, [3, 8, 36, 3], num_classes=num_classes)


if __name__ == '__main__':
    # summary(resnet34(), (1, 3, 224, 224))
    summary(models.resnet34(), (1, 3, 224, 224))

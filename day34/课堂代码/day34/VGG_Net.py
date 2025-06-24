"""
搭建VGG网络：
   共性的： 全连接层， VGG11  VGG13  VGG16  VGG19 都使用相同的全连接层
   卷积层是变化的， 所以需要参数来控制

经验：
    1. 卷积层最终交给全连接层的时候， 图像数据的形状一般都设置成 10*10及以下的尺寸， 比如： 5*5  7*7
    2. 很多经典神经网络中都采用的是小卷积核
"""
import torch.nn as nn
import torch


class VGG(nn.Module):

    def __init__(self, features, num_classes=1000, dropout=0.5):
        super().__init__()
        # 卷积层 -- 提取特征
        # features 是传入的卷积层
        self.features = features
        self.adaptive_avgpool = nn.AdaptiveAvgPool2d((7, 7))
        # 全连接层 -- 分类
        self.classifier = nn.Sequential(
            nn.Linear(in_features=512 * 7 * 7, out_features=4096),
            nn.ReLU(True),
            # Dropout在全连接层使用
            nn.Dropout(p=dropout),
            nn.Linear(in_features=4096, out_features=4096),
            nn.ReLU(True),
            nn.Dropout(p=dropout),
            nn.Linear(in_features=4096, out_features=num_classes)
        )

    def forward(self, data):
        # 将data交给卷积层
        x = self.features(data)
        # 将卷积层的输出交给自适应平均池化， 将图像尺寸设置成了 7 * 7
        x = self.adaptive_avgpool(x)
        # 将自适应平均池化输出的数据展开成NV结构
        x = torch.flatten(x, 1)
        # 将NV结构的数据交给全连接层
        x = self.classifier(x)
        return x


# 定义各种VGG网络的卷积层参数
vgg_config = {
    "vgg11": [64, "M", 128, "M", 256, 256, "M", 512, 512, "M", 512, 512, "M"],
    "vgg13": [64, 64, "M", 128, 128, "M", 256, 256, "M", 512, 512, "M", 512, 512, "M"],
    "vgg16": [64, 64, "M", 128, 128, "M", 256, 256, 256, "M", 512, 512, 512, "M", 512, 512, 512, "M"],
    "vgg19": [64, 64, "M", 128, 128, "M", 256, 256, 256, 256, "M", 512, 512, 512, 512, "M", 512, 512, 512, 512, "M"],
}


def make_layers(cfg, batch_norm: bool = False) -> nn.Sequential:
    # 存储卷积层和池化层
    layers = []
    in_channels = 3
    for v in cfg:
        if v == "M":
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            if batch_norm:
                # BatchNorm2d常规用法： 添加在激活函数之前， 也就是线性和非线性之间
                # nn.BatchNorm1d: 使用在全链接中， 基本不使用
                layers += [conv2d, nn.BatchNorm2d(v), nn.ReLU(inplace=True)]
            else:
                layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
    return nn.Sequential(*layers)


def vgg11(batch_norm=True, num_classes=1000, dropout=0.5):
    return VGG(make_layers(vgg_config["vgg11"], batch_norm), num_classes, dropout)


def vgg13(batch_norm=True, num_classes=1000, dropout=0.5):
    return VGG(make_layers(vgg_config["vgg13"], batch_norm), num_classes, dropout)


def vgg16(batch_norm=True, num_classes=1000, dropout=0.5):
    return VGG(make_layers(vgg_config["vgg16"], batch_norm), num_classes, dropout)


def vgg19(batch_norm=True, num_classes=1000, dropout=0.5):
    return VGG(make_layers(vgg_config["vgg19"], batch_norm), num_classes, dropout)

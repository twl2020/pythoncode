"""
该模块的作业： 搭建模型
"""
import torch.nn as nn


class MnistNet(nn.Module):

    def __init__(self):
        super().__init__()
        # Sequential: 将模型的组件和搭建模型合二为一
        self.layer = nn.Sequential(
            nn.Linear(28 * 28, 500),
            nn.ReLU(),
            nn.Linear(500, 300),
            nn.ReLU(),
            nn.Linear(300, 100),
            nn.ReLU(),
            nn.Linear(100, 50),
            nn.ReLU(),
            nn.Linear(50, 10)
        )

    def forward(self, data):
        # 传入data图像数据形状是（N，C, H, W）
        # 全连接神经网络接收的数据形状是： NV
        data = data.view(data.size(0), -1)
        out = self.layer(data)
        return out

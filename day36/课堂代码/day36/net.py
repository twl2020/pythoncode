"""
搭建网络模型
"""

import torch.nn as nn


class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            # (N, 3, 224, 224)  --  (N, 64, 224, 224)
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            # (N, 3, 224, 224)  --  (N, 64, 112, 112)
            nn.MaxPool2d(2),

            # (N, 64, 112, 112)  --  (N, 64, 112, 112)
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            # (N, 64, 112, 112)  --  (N, 64, 56, 56)
            nn.MaxPool2d(2),

            # (N, 64, 56, 56)  --  (N, 128, 56, 56)
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            # (N, 128, 56, 56)  --  (N, 128, 28, 28)
            nn.MaxPool2d(2),

            # (N, 128, 28, 28)  --  (N, 256, 28, 28)
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            # (N, 256, 28, 28)  --  (N, 256, 14, 14)
            nn.MaxPool2d(2),

            # (N, 256, 14, 14)  --  (N, 256, 14, 14)
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            # (N, 256, 14, 14)  --  (N, 256, 7, 7)
            nn.MaxPool2d(2),

            # (N, 256, 7, 7)  --  (N, 512, 7, 7)
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            # (N, 512, 7, 7)  --  (N, 512, 3, 3)
            nn.MaxPool2d(2)
        )

        self.classifier = nn.Sequential(
            # 将NCHW 变成 NV
            nn.Flatten(),
            # 512 * 3 * 3 = 4608
            nn.Linear(in_features=4608, out_features=2048),
            nn.ReLU(True),
            nn.Linear(in_features=2048, out_features=512),
            nn.ReLU(True),
            nn.Linear(in_features=512, out_features=1)
        )

        self.regression = nn.Sequential(
            # 将NCHW 变成 NV
            nn.Flatten(),
            # 512 * 3 * 3 = 4608
            nn.Linear(in_features=4608, out_features=2048),
            nn.ReLU(True),
            nn.Linear(in_features=2048, out_features=512),
            nn.ReLU(True),
            nn.Linear(in_features=512, out_features=4)
        )

    def forward(self, data):
        # 将输入的数据交给卷积层提取特征
        x = self.features(data)
        label = self.classifier(x)
        loc = self.regression(x)
        return label, loc

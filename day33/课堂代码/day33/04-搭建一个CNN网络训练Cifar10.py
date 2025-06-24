from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch.nn as nn
from torch import optim
import tqdm


class CNN(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            # 输入通道数 = 卷积核的通道数
            # 输出通道数 = 卷积核的个数
            # 上一层的输出 作为 下一层的输入
            # (N, 1, 28, 28)  --> (N, 10, 26, 26)
            # 卷积
            nn.Conv2d(in_channels=1, out_channels=10, kernel_size=3),
            nn.ReLU(inplace=True),
            # (N, 10, 26, 26)  --> (N, 6, 24, 24)
            # 卷积
            nn.Conv2d(in_channels=10, out_channels=6, kernel_size=3),
            nn.ReLU(inplace=True),
            # (N, 6, 24, 24)  --> (N, 6, 12, 12)
            # 池化
            nn.MaxPool2d(kernel_size=2, stride=2),
            # (N, 6, 12, 12)  --> (N, 4, 10, 10)
            # 卷积
            nn.Conv2d(in_channels=6, out_channels=4, kernel_size=3),
            nn.ReLU(inplace=True),
            # (N, 4, 10, 10)  --> (N, 4, 8, 8)
            # 卷积
            nn.Conv2d(in_channels=4, out_channels=4, kernel_size=3),
            nn.ReLU(inplace=True),

            # 全连接层 -- 做十分类
            # (N, C, H, W)  -- (N, V)
            nn.Flatten(),
            nn.Linear(in_features=4 * 8 * 8, out_features=128),
            nn.ReLU(inplace=True),
            nn.Linear(in_features=128, out_features=32),
            nn.ReLU(inplace=True),
            nn.Linear(in_features=32, out_features=10)
        )

    def forward(self, data):
        out = self.layer(data)
        return out


if __name__ == '__main__':
    dataset = datasets.MNIST(root="data", train=True, download=True, transform=transforms.ToTensor())
    train_loader = DataLoader(dataset=dataset, batch_size=100, shuffle=True)

    epoches = 1000
    # 创建模型
    net = CNN()
    # 损失函数
    loss_fn = nn.CrossEntropyLoss(reduction="sum")
    optimizer = optim.Adam(net.parameters())

    for epoch in tqdm.tqdm(range(epoches)):
        # 记录每一轮训练的总损失
        train_total_loss = 0
        for images, labels in train_loader:
            logits = net(images)
            loss = loss_fn(logits, labels)
            train_total_loss += loss
            # BP算法
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        # 每一轮训练完成后， 计算总样本的平均损失
        avg_train_loss = train_total_loss / len(dataset)
        print(f"epoch:{epoch}, loss:{avg_train_loss}")

        # 每一轮训练完成后计算总的准确率

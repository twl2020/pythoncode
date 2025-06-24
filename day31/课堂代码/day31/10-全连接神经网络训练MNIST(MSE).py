import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

"""
使用全连接神经网络进行十分类任务

MSE对概率值不敏感， 所以多分类的时候选择 交叉熵损失函数
交叉熵损失函数对概率值比较敏感
"""


class MnistNet(nn.Module):

    def __init__(self):
        super().__init__()
        # 图像的一个像素点就是一个特征
        self.layer01 = nn.Linear(28 * 28, 512)
        self.layer02 = nn.Linear(512, 256)
        self.layer03 = nn.Linear(256, 128)
        self.layer04 = nn.Linear(128, 64)
        self.layer05 = nn.Linear(64, 32)
        self.layer06 = nn.Linear(32, 10)
        self.relu = nn.ReLU()

    def forward(self, data):
        data = self.relu(self.layer01(data))
        data = self.relu(self.layer02(data))
        data = self.relu(self.layer03(data))
        data = self.relu(self.layer04(data))
        data = self.relu(self.layer05(data))
        out = self.layer06(data)
        out = nn.functional.softmax(out, dim=-1)
        return out


if __name__ == '__main__':
    # 定义批次大小
    batch_size = 100
    # 训练轮次
    epoches = 2000
    # 学习率
    learn_rate = 0.1
    # 加载MNIST数据集
    dataset = datasets.MNIST(root="data", train=True, download=True, transform=transforms.ToTensor())
    # 使用加载器分批次加载数据
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)
    # 创建模型对象
    net = MnistNet()
    # 创建损失函数
    loss_fn = nn.MSELoss()

    for epoch in range(epoches):
        # 迭代train_loader， 得到数据
        # images： 每个批次加载的图片数据   --- 交给模型的数据
        # labels： 每个批次加载的图片数据所对应的标签
        for images, labels in train_loader:
            # labels的形状是: (100, )
            # 使用MSE之后需要手动的将labels进行one-hot， 这样形状才能和pred_y的形状对应上
            labels = nn.functional.one_hot(labels, 10).float()
            # images的形状是 (N, C, H, W) 需要变成 NV结构
            images = images.reshape(images.size(0), -1)
            # pred_y的形状： (100, 10)
            pred_y = net(images)
            # 计算损失
            loss = loss_fn(pred_y, labels)
            # 梯度清零
            net.zero_grad()
            # 反向传播
            loss.backward()
            # 更新参数
            for parameter in net.parameters():
                parameter.data -= learn_rate * parameter.grad

            print(f"epoch:{epoch}, loss:{loss}")

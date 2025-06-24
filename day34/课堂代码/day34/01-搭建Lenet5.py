"""
学习经典CNN目的是学习CNN的思想， 指导我们自定义网络。
不是让我们照搬网络， 因为经典CNN在不同的数据集上表现也不一样。
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch import optim
from torchinfo import summary


class Lenet5(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            # (N, 1, 28, 28)   -- (N, 6, 28, 28)
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, padding=2),
            nn.Tanh(),
            # (N, 6, 28, 28) --  (N, 6, 14, 14)
            nn.AvgPool2d(kernel_size=2),
            # (N, 6, 14, 14)  -- (N, 16, 10, 10)
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5),
            nn.Tanh(),
            #  (N, 16, 10, 10)  -- (N, 16, 5, 5)
            nn.AvgPool2d(kernel_size=2),
            # (N, 16, 5, 5) -- (N, 120, 1, 1)
            nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5),
            nn.Tanh(),

            # 全连接层
            # 卷积层的数据形状： (N, C, H, W)
            # 全连接层接收的数据形状是：(N, V)
            nn.Flatten(),
            nn.Linear(in_features=120, out_features=84),
            nn.Tanh(),
            nn.Linear(in_features=84, out_features=10)
        )

    def forward(self, data):
        out = self.layers(data)
        return out


def train():
    # batch_size
    batch_size = 100
    # 定义训练的轮次
    epoches = 1000
    train_dataset = datasets.MNIST(root="data", train=True, download=True,
                                   transform=transforms.ToTensor())

    test_dataset = datasets.MNIST(root="data", train=False, download=True,
                                  transform=transforms.ToTensor())

    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size)

    # 创建模型对象
    net = Lenet5()
    # 定义交叉熵损失函数
    loss_fn = nn.CrossEntropyLoss(reduction="sum")
    # 优化器
    optimizer = optim.Adam(net.parameters())

    for epoch in range(epoches):
        # 设置成训练模式
        net.train()
        # 定义一个变量， 存储每一轮训练样本的总损失
        train_total_loss = 0
        # 定义一个变量， 存储每一轮测试样本的总损失
        test_total_loss = 0
        # 以下的循环代码， 循环一次是做什么操作？？？
        # 循环一次得到一个批次的数据
        for images, labels in train_loader:
            # 将样本图像数据交给模型训练， 得到模型输出的结果
            logits = net(images)
            # 使用损失函数计算预测值和真实值的损失
            loss = loss_fn(logits, labels)
            train_total_loss += loss
            # BP算法
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # 训练完一轮后输出总样本的平均损失
        train_avg_loss = train_total_loss / len(train_dataset)

        # 一轮训练完成后使用测试集验证模型， 使用测试计算模型的总准确率
        net.eval()  # 评估模式
        with torch.no_grad():
            # 用来记录预测准确的样本总数
            correct = 0
            for test_images, test_labels in test_loader:
                test_logits = net(test_images)
                test_loss = loss_fn(test_logits, test_labels)
                test_total_loss += test_loss

                # 计算模型预测正确的样本总数
                pred = torch.argmax(test_logits, dim=-1)

                # 现在pred预测类别和test_labels真实类别的形状一样， 都是(100, )
                # 所以使用pred和test_labels进行逐元素比较， 得到的结果中True表示预测准确的样本；False预测错误的样本
                # 计算模型预测正确的样本总数：直接将比较的结果累加即可， True: 1  False: 0
                correct += torch.sum(pred == test_labels)

            # 每一轮测试完成后输出测试总样本的平均损失
            test_avg_loss = test_total_loss / len(test_dataset)

            # 每一轮测试完成后计算准确率
            correct_rate = correct * 100 / len(test_dataset)
            print(f"epoch:{epoch}, train_loss:{train_avg_loss}, test_loss:{test_avg_loss}, 准确率：{correct_rate}")


if __name__ == '__main__':
    # train()
    # 创建模型对象
    net = Lenet5()
    summary(net, input_size=(1, 1, 28, 28))

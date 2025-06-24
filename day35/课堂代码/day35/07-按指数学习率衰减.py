import torch
from torch import optim
import matplotlib.pyplot as plt


def test_ExponentialLR():
    # 0.参数初始化
    LR = 0.1  # 设置学习率初始化值为0.1
    iteration = 10
    max_epoch = 200
    # 1 初始化参数
    y_true = torch.tensor([0])
    x = torch.tensor([1.0])
    w = torch.tensor([1.0], requires_grad=True)
    # 2.优化器
    optimizer = optim.SGD([w], lr=LR, momentum=0.9)
    # 3.设置学习率下降策略
    scheduler_lr = optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.95)
    # 4,获取学习率的值和当前的epoch
    lr_list = list()
    epoch_list = list()
    for epoch in range(max_epoch):
        # 获取当前lr
        lr_list.append(scheduler_lr.get_last_lr())
        # 获取当前的epoch
        epoch_list.append(epoch)
        # 遍历每一个batch数据
        for i in range(iteration):
            # 目标函数
            loss = ((w * x - y_true) ** 2) / 2.0
            # 梯度清零
            optimizer.zero_grad()
            # 反向传播
            loss.backward()
            # 参数更新
            optimizer.step()
        # 更新下一个epoch的学习率
        scheduler_lr.step()
    # 5.绘制学习率变化的曲线
    plt.plot(epoch_list, lr_list, label="ExponentialLR Scheduler")
    plt.xlabel("Epoch")
    plt.ylabel("Learning rate")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # test_StepLR()
    # test_MultiStepLR()
    test_ExponentialLR()

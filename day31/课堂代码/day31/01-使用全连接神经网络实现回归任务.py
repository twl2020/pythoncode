import numpy as np
import torch
from torch import nn
import matplotlib.pyplot as plt


# 搭建5层全连接神经网络
class MLP(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer01 = nn.Linear(1, 300)
        self.layer02 = nn.Linear(300, 200)
        self.layer03 = nn.Linear(200, 100)
        self.layer04 = nn.Linear(100, 50)
        self.layer05 = nn.Linear(50, 1)
        self.relu = nn.ReLU()

    def forward(self, data):
        data = self.relu(self.layer01(data))
        data = self.relu(self.layer02(data))
        data = self.relu(self.layer03(data))
        data = self.relu(self.layer04(data))
        out = self.layer05(data)
        return out


if __name__ == '__main__':
    # 固定随机数的种子， 目的是为了重复实验
    np.random.seed(42)
    # 样本数据， X的形状: (100, 1)
    # 100表示  样本数量
    # 1表示 特征数量
    X = np.random.rand(100, 1) * 10
    # 样本数据， Y就是真实值
    Y = np.sin(X) + 0.1 * np.random.randn(100, 1)
    # 将numpy数组转成了 tensor
    # 为什么这里需要将tensor中元素的数据类型设置成float32
    # 因为这里的X需要和W加权求和， 而W是float32类型， 所以需要X和W相同的类型
    x_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(Y, dtype=torch.float32)

    # 测试数据，当模型训练完成后，使用该数据进行测试，
    # 如果测试数据和样本数据的真实值很接近， 说明模型训练完成
    X_test = torch.FloatTensor(np.linspace(0, 10, 100).reshape(-1, 1))

    # 训练模型
    epoches = 5000
    # 定义一个学习率
    learn_rate = 0.1
    # 创建模型对象
    net = MLP()
    # 创建损失函数
    mse_loss = nn.MSELoss()

    for epoch in range(epoches):
        # 使用模型前向传播进行训练
        pred_y = net(x_tensor)
        # 使用预测值和真实值计算损失
        loss = mse_loss(pred_y, y_tensor)
        print(f"epoch:{epoch}, loss:{loss}")
        # 梯度清零
        net.zero_grad()
        # 使用loss进行反向传播， 计算梯度
        loss.backward()
        # 使用梯度更新参数: w和b
        # 所有的参数都在net中
        for parameter in net.parameters():
            parameter.data -= learn_rate * parameter.grad

    # 循环完成， 模型就训练完成， 也就是说现在net是训练好的模型（也就是net中的w和b已经训练出结果了）
    # 模型训练完成后就可以使用测试数据验证模型的效果
    with torch.no_grad():
        Y_test = net(X_test)

    # 绘制可视化效果， 观察数据的拟合效果
    plt.scatter(x_tensor.detach().numpy(), y_tensor.detach().numpy())
    # 绘制预测结果的散点图
    plt.scatter(X_test, Y_test, color="red")
    plt.show()



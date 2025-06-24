"""
使用pytorch改进之前的非线性回归
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import torch

# 准备数据
_x = [ele / 100 for ele in range(100)]
_y = [3 * np.sin(5 * ele) + ele * 2 + 10 + random.random() for ele in _x]

# 定义训练的轮次
epochs = 10000
# 学习率
learn_rate = 0.1

# 初始化w, w是我们这里的叶子节点
weights = torch.tensor([random.random() for _ in range(6)], requires_grad=True)

for epoch in range(epochs):
    # x 和 y是已知数据
    for x, y in zip(_x, _y):
        # 使用模型得到预测值, pred_y是一个标量值
        powers = torch.tensor([x ** n for n in range(5, -1, -1)])
        pred_y = torch.dot(weights, powers)
        # 使用预测值和真实值计算损失
        loss = (pred_y - y) ** 2

        # 梯度清零; 反向传播，计算梯度; 使用梯度更新参数  就是我们后面说的BP算法
        # 梯度清零
        if weights.grad is not None:
            weights.grad.data.zero_()
        # 反向传播，计算梯度
        loss.backward()

        # 使用梯度更新参数
        weights.data -= learn_rate * weights.grad

    # 每一轮打印的损失，其实是最后一个点的损失值， 不能反映整体的损失
    print(f"epoch:{epoch}, loss:{loss}")
    if epoch % 10 == 0:
        # 训练完成一轮后， 可视化拟合效果
        plt.cla()
        plt.scatter(_x, _y)
        # 绘制拟合曲线
        plt.plot(_x,
                 [weights[0].item() * x ** 5 + weights[1].item() * x ** 4 + weights[2].item() * x ** 3 + weights[
                     3].item() * x ** 2 + weights[4].item() * x + weights[5].item() for x in _x],
                 color="red")
        plt.pause(0.1)

plt.show()

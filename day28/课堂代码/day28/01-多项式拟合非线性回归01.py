"""
使用泰勒展开的思想： 使用一个多项式展开拟合数据

方式一： 计算单个点的损失

耗时：78.68057107925415
epoch:688, loss:0.10524866065127039

分析：
  1. 样本数据是一个非线性的， 所以不能使用线性模型（因为目前我们还没有使用激活函数），
  此时我们可以定义一个N次多项式进行拟合， 目前N我设计成5   -- 模型就有了
  w1 * x**5 + w2 * x ** 4 + w3 * x ** 3 + w4 * x ** 2 + w5 * x + w6

  2. 计算损失 -- 计算单个点的损失
  3. 计算梯度
  4. 更新参数
"""
import numpy as np
import random
import matplotlib.pyplot as plt
import time

# 准备数据
_x = [ele / 1000000 for ele in range(1000000)]
_y = [3 * np.sin(5 * ele) + ele * 2 + 10 + random.random() for ele in _x]

_x = np.array(_x)
_y = np.array(_y)

# 定义训练的轮次
epochs = 10000
# 学习率
learn_rate = 0.1

# 初始化w
w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()
w5 = random.random()
w6 = random.random()

# 开始时间
start = time.time()

for epoch in range(epochs):
    # x 和 y是已知数据
    for x, y in zip(_x, _y):
        # 使用模型得到预测值, pred_y是一个标量值
        pred_y = w1 * x ** 5 + w2 * x ** 4 + w3 * x ** 3 + w4 * x ** 2 + w5 * x + w6
        # 使用预测值和真实值计算损失
        loss = (pred_y - y) ** 2
        # 计算梯度, grad是复合函数中外层函数得到的梯度  -- dloss / dpred_y
        grad = 2 * (pred_y - y)
        # 还需要对w进行求导  dpred_y/dw
        grad_w1 = grad * x ** 5
        grad_w2 = grad * x ** 4
        grad_w3 = grad * x ** 3
        grad_w4 = grad * x ** 2
        grad_w5 = grad * x
        grad_w6 = grad

        # 使用梯度更新参数
        w1 -= learn_rate * grad_w1
        w2 -= learn_rate * grad_w2
        w3 -= learn_rate * grad_w3
        w4 -= learn_rate * grad_w4
        w5 -= learn_rate * grad_w5
        w6 -= learn_rate * grad_w6

    # 每一轮打印的损失，其实是最后一个点的损失值， 不能反映整体的损失
    print(f"epoch:{epoch}, loss:{loss}")
    if epoch % 10 == 0:
        # 训练完成一轮后， 可视化拟合效果
        plt.cla()
        plt.scatter(_x, _y)
        # 绘制拟合曲线
        plt.plot(_x,
                 [w1 * x ** 5 + w2 * x ** 4 + w3 * x ** 3 + w4 * x ** 2 + w5 * x + w6 for x in _x],
                 color="red")
        plt.pause(0.1)

    # 每一轮结束时间
    stop = time.time()
    print(f"耗时：{stop - start}")
plt.show()

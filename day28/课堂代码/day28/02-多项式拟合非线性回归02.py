"""
使用泰勒展开的思想： 使用一个多项式展开拟合数据

方式二： 计算总体的平均损失  -- mse

分析：
  1. 样本数据是一个非线性的， 所以不能使用线性模型（因为目前我们还没有使用激活函数），
  此时我们可以定义一个N次多项式进行拟合， 目前N我设计成5   -- 模型就有了
  w1 * x**5 + w2 * x ** 4 + w3 * x ** 3 + w4 * x ** 2 + w5 * x + w6

  2. 计算损失 -- 计算总体的平均损失  -- mse
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
epochs = 100000
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
    # 使用模型得到预测值, pred_y是一维数组
    pred_y = w1 * _x ** 5 + w2 * _x ** 4 + w3 * _x ** 3 + w4 * _x ** 2 + w5 * _x + w6
    # 计算损失  mse
    losses = (pred_y - _y) ** 2
    loss = np.mean(losses)
    # 计算梯度
    # 2 * (pred_y - _y) 得到也是向量， 也就是每个样本点的梯度值
    # 因为每个样本点的梯度值不能反映整体的梯度
    # 每个样本点的梯度值 / len(_y)  -- 反映了单个梯度对整体样本的贡献
    # grad -- 向量
    # _x ** 5 也是向量
    grad = 2 * (pred_y - _y) / len(_y)
    # 对w求导
    grad_w1 = np.dot(grad, _x ** 5)
    grad_w2 = np.dot(grad, _x ** 4)
    grad_w3 = np.dot(grad, _x ** 3)
    grad_w4 = np.dot(grad, _x ** 2)
    grad_w5 = np.dot(grad, _x)
    grad_w6 = np.sum(grad)

    # 更新参数
    w1 -= learn_rate * grad_w1
    w2 -= learn_rate * grad_w2
    w3 -= learn_rate * grad_w3
    w4 -= learn_rate * grad_w4
    w5 -= learn_rate * grad_w5
    w6 -= learn_rate * grad_w6

    print(f"epoch: {epoch}, loss:{loss}")
    # 可视化
    if epoch % 10 == 0:
        # 可视化
        plt.cla()
        plt.scatter(_x, _y)
        plt.plot(_x, pred_y, color="red")
        plt.pause(0.1)

plt.show()

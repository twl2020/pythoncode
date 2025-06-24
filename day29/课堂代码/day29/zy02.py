import random
import numpy as np
import torch
import matplotlib.pyplot as plt

# 准备数据
_x = np.array([ele / 100 for ele in range(100)])
list_y = np.array([3 * np.sin(5 * ele) + ele * 2 + 10 + random.random() for ele in _x])
_y = torch.tensor(list_y)

w_list = torch.full((6,), 3.0, dtype=torch.float32, requires_grad=True)


step = 0.1
epoches = 100000
for i in range(epoches):
    # 模型函数
    X = [_x ** 5, _x ** 4, _x ** 3, _x ** 2, _x, _x**0]
    y_h = w_list @ torch.tensor(X, dtype=torch.float32, requires_grad=True)
    # 损失函数
    mse_loss = torch.mean((y_h - _y) ** 2)
    if w_list.grad is not None:
        w_list.grad.zero_()

    # 更新参数
    y_h.retain_grad()
    mse_loss.backward()
    with torch.no_grad():
        w_list -= w_list.grad * step
    print(f'轮次：{i}, loss={mse_loss.item():.6f}, 权重：{w_list}')
    if i % 100 == 0:
        plt.cla()
        plt.scatter(_x, list_y)
        plt.plot(_x, y_h.detach().numpy(), color='red', label=f'loss={mse_loss.item()}')
        plt.pause(0.1)
plt.show()

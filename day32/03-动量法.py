import torch

# 1 初始化权重参数
w = torch.tensor([3.0], requires_grad=True, dtype=torch.float32)
y = w ** 2 / 2.0
z = y.sum()

# 2 实例化优化⽅法: SGD指定参数beta=0.9
# 交给优化器的params参数必须是一个tensor的可迭代对象， 所以使用[]将w包起来
# momentum这个表示的动量， 其实就是指数加权平均中的 beta值
# lr是learn_rate学习率的缩写。 默认是0.001
optimizer = torch.optim.SGD([w], lr=0.01, momentum=0.9)
# 3 第1次更新 计算梯度,并对参数进⾏更新
# 梯度清零， 反向求导、更新参数 构成了 BP算法
optimizer.zero_grad()
z.backward()
optimizer.step()

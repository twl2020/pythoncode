import torch

x = torch.tensor(3.0, requires_grad=True)
y = x ** 2
z = 3 * y + 6
print(y)
# 反向就是求导
# y.backward()
# print(x.grad)
# print(y.grad_fn)
# 中间节点要向获取导数， 必须调用retain_grad()进行保留， 否则无法获取
# retain_grad() 必须在 backward() 函数前执行
y.retain_grad()
z.backward()
print(x.grad)
print(y.grad)

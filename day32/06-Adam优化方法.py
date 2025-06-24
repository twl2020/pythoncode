import torch

# 1 初始化权重参数
w = torch.tensor([3.0], requires_grad=True, dtype=torch.float32)
y = w ** 2 / 2.0
z = y.sum()


optimizer = torch.optim.Adam([w])

optimizer.zero_grad()
z.backward()
optimizer.step()

print(w.grad)

import torch

# t1 = torch.zeros((2, 3), device="cuda:0")
# t1 = torch.ones((2, 3), device="cuda:0")
t1 = torch.empty((2, 3), device="cuda:0")

print(t1)
t2 = torch.fill(t1, 100)
print(t2)

# 在pytorch中 xxx_的函数就是 in-place 函数
torch.fill_(t1, 200)
print(t1)
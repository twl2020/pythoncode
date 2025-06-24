import torch

t1 = torch.arange(1, 13)
t1 = torch.reshape(t1, (3, 4))
print(t1)
print(torch.sum(t1))  # 没有指定dim维度， 就是将张量当作一维进行求和
print(torch.sum(t1, dim=0, keepdim=True))
print(torch.sum(t1, dim=1, keepdim=True))

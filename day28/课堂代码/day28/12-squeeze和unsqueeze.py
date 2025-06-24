import torch

t1 = torch.arange(1, 13).reshape((1, 3, 4))
print(t1)
print(t1.shape)

t2 = torch.squeeze(t1)
print(t2.shape)
t3 = torch.unsqueeze(t2, dim=0)
print(t3.shape)

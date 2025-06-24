import torch
import torch.nn as nn

data = torch.arange(1, 17)

data = torch.reshape(data, (1, 1, 4, 4)).float()

# pool1 = nn.MaxPool2d(kernel_size=2, stride=2)  # 最大池化，stride缺省值2
pool1 = nn.AvgPool2d(kernel_size=2, stride=2)  # 最大池化，stride缺省值2

x = pool1(data)
print(data.shape), print(x.shape)
print(data), print(x)

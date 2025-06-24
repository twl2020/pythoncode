import torch
import torch.nn.functional as F
from torch.nn import Parameter

weight = torch.tensor([[2, 0, 1],
                       [0, 1, 2],
                       [1, 0, 2]], dtype=torch.float32)
# N C H W
weight = weight.reshape(1, 1, 3, 3)
# 类型转换
weight = Parameter(weight)
conv = torch.nn.Conv2d(1, 1, kernel_size=3, padding=1, bias=False)
# # 使用卷积运算之前先赋值
conv.weight = weight
data = torch.tensor([[1, 2, 3, 0],
                     [0, 1, 2, 3],
                     [3, 0, 1, 2],
                     [2, 3, 0, 1]], dtype=torch.float32)
# # N C H W
data = data.reshape(1, 1, 4, 4)
feature_map = conv(data)
# print(feature_map.shape)
# # result = F.conv2d(input=data, weight=weight, stride=1)
result = F.conv2d(input=data, weight=weight, stride=1, padding=1)
print(result.shape)
print(result)
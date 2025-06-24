"""
连续张量： 也就是张量中的元素在内存中是连续存储的
"""
import torch

x = torch.arange(1, 13).reshape(3, 4)
print(x)
# is_contiguous(): 判断张量是否连续
print(x.is_contiguous())
# 切片操作会将张量变成不连续的张量
y = x[:, 0:2]
print(y)
print(y.is_contiguous())
# 将不连续的张量变成连续张量
z = y.contiguous()
print(z)
print(z.is_contiguous())

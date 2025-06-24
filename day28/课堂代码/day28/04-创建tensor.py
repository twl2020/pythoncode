"""
tensor: 张量
"""
import torch
import numpy as np

# 创建张量
# Tensor()创建的张量的元素类型是float32,不能更改; 不能更改device,只能使用默认的cpu
# Tensor(标量)： 标量表示的是一维张量的元素的个数
# t1 = torch.Tensor(0)
# Tensor(元组或列表或ndarray)：这里的元素或列表中的内容就是张量的内容
# t1 = torch.Tensor([1, 3, 4])
# t1 = torch.Tensor([[1, 3], [4, 5]])
arr = np.array([[1, 3], [4, 5]])
# t1 = torch.Tensor(arr)  # device没有指定，默认就是cpu
# t1 = torch.Tensor(arr, device="cpu")

t1 = torch.Tensor(arr)
print(t1.dtype)
print(t1)

print("-----------------------------------------------------------")
# tensor(标量)： tensor张量中存储的就是这个标量值
# t2 = torch.tensor(10)
# tensor(元组或列表或ndarry)： tensor张量中存储的就是元组或列表或ndarry的元素
# 总结： tensor()中的值就是存储在tensor的元素
# t2 = torch.tensor([1, 2, 3], device="cuda:0", dtype=torch.float32)
t2 = torch.FloatTensor([1, 2, 3])  # 默认使用cpu
# t2 = t2.cuda()  # 将tensor使用cuda计算
t2 = t2.to("cuda") #  # 将tensor使用cuda计算
print(t2.dtype)
print(t2)

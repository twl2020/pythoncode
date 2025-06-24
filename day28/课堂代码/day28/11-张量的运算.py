import torch

# 加减乘除运算是逐元素操作的
t1 = torch.arange(1, 13).reshape(3, 4)
t2 = torch.ones_like(t1)
print(t1 + t2)

print("-----------------一维-------------------------")
t1 = torch.tensor([1, 2, 3])
t2 = torch.tensor([4, 5, 6])
# @ 表示点乘， 维度必须 >= 1
# @ 会根据维度的不同重载不同的函数
print(t1 @ t2)
# pytorch中dot点乘只能同于一维上
print(t1.dot(t2))
print(torch.dot(t1, t2))

print("-------------------二维-----------------------")
t1 = torch.tensor([[1, 2, 3], [1, 2, 3]])
t2 = torch.tensor([[4, 5, 6], [4, 5, 6]])
t2 = torch.transpose(t2, 1, 0)
# pytorch中矩阵的乘法需要使用 mm() 或者 matmul()
# mm()只能用于二维张量（矩阵）的点乘
# print(t1 @ t2)
# print(t1.mm(t2))
print(torch.mm(t1, t2))
print(torch.matmul(t1, t2))

print("-------------------三维-----------------------")
# 高维使用矩阵乘法要求：
# 最后两个维度的形状必须满足矩阵相乘的形状要求
# 剩余维度对应的长度要么相同， 要么有一个是1
# 2,1,3
t1 = torch.tensor([[[1, 2, 3]], [[1, 2, 3]]])
# (2, 3, 1)
t2 = torch.tensor([[[4], [5], [6]], [[4], [5], [6]]])

print(t1 @ t2)
print(torch.matmul(t1, t2))

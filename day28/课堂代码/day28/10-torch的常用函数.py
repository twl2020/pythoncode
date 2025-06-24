"""
 torch的常用函数:
    torch.numel(a) # 返回张量中元素的个数
    torch.eye(5) # 创建 5 * 5张量，对角线为1
    a.item() # 张量是一个数的时候才能使用
    a.int() # 张量转换为int（float、short、long）类型
    torch.transpose(a, 0, 1) # 交换一个tensor的两个维度
"""
import torch

t1 = torch.arange(1, 13).reshape(3, 4)
print(t1)
# numel == number  element
print(t1.numel())

t2 = torch.eye(5)
print(t2)

# tensor对象.int() 将元素的类型转成int
t3 = t2.int()
print(t3)

# item()
t4 = torch.arange(1, 13).reshape(3, 4)
# tensor中存储的是标量，才能使用item()
# print(torch.sum(t4))  # tensor(78)
print(torch.sum(t4).item())  # 78



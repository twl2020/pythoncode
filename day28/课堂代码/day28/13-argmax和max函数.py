import torch

t1 = torch.arange(1, 13).reshape(3, 4)
print(t1)
# argmax(): 返回最大值的索引
index = torch.argmax(t1, dim=0)
print(index)
print("========================================")
# max(): 函数, 没有指定dim的时候返回的是所有元素的最大值
# max(dim=0)： 如果指定的dim维度， 返回的是元组： 包含对应轴上的最大值及其索引
m, index = torch.max(t1, dim=0)
print(m)
print(index)



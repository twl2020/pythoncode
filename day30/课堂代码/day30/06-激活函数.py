import torch
from torch.nn import functional as F
import matplotlib.pyplot as plt

data = torch.linspace(-10, 10, steps=50)

# res = torch.sigmoid(data)
# res = torch.relu(data)
# print(res)
# res01 = F.sigmoid(data)
# res01 = F.relu(data)
# print(res01)

# s是Sigmoid类的对象
# s = torch.nn.Sigmoid()
# s = torch.nn.ReLU()
s = torch.nn.LeakyReLU()
# 对象() 可以使用这种方式的前提是: 该对象必须是一个可调用对象， 也就是该类重写 __call__()方法
# Sigmoid的父类是Module类， Module类重写__call__()方法， 所以Module类的子类对象都是可调用对象
res03 = s(data)
plt.plot(data, res03)

plt.grid(True)

plt.show()

print(res03)

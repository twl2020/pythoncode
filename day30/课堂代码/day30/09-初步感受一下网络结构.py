"""
初步搭建一个全连接神经网络， 注意， 这里的神经网络是没有加训练过程

多层的全连接神经网络也叫做多层感知机  MLP

我们使用 pytorch框架搭建神经网络， 必须继承 torch.nn.Module

搭建神经网络就 跟大家生活中 搭积木是一样的
1. 准备搭建网络的组件
2. 使用组件搭建网络
"""
import torch
import torch.nn as nn


# 搭建一个3层的全连接神经网络
class MLP(nn.Module):

    def __init__(self):
        super().__init__()
        # 准备搭建网络的组件
        self.layer01 = nn.Linear(2, 9)
        self.layer02 = nn.Linear(9, 5)
        self.layer03 = nn.Linear(5, 1)
        self.relu = nn.ReLU()

    # 使用组件搭建网络
    # data就是交给模型的数据
    def forward(self, data):
        # 将输入的数据交给模型的第一层
        data = self.layer01(data)
        # 将模型第一层的输出交给激活函数
        data = self.relu(data)
        # 将激活函数的结果交给模型的第二层
        data = self.layer02(data)
        data = self.relu(data)
        out = self.layer03(data)
        # out就是模型输出的最终结果
        return out


"""
  全连接神经网络中输入的数据形状必须是： (N, V)结构
  N: 表示每个批次的样本数量   Number
  V: 表示的就是每个样本的一维数据     Vector
  
   比如将一张RGB图像交给全连接神经网络， 那么输入的数据形状就是： (1, h*w*c)
  
"""
if __name__ == '__main__':
    # 样本数据需要和权重进行加权求和的运算， w的类型是浮点数， 所以这里的样本数据需要设置成float
    # 样本数据
    # (1, 2)    -- (1, 2)
    # data = torch.tensor([1, 3], dtype=torch.float32)
    # (1, 2)  -- (1, 2)
    # data = torch.tensor([[1, 3]], dtype=torch.float32)
    # (1, 1, 2)   -- (1, 1*2)
    # data = torch.tensor([[[1, 3]]], dtype=torch.float32)
    # (1, 1, 1, 2) -- (1, 1*1*2)
    data = torch.tensor([[[[1, 3]]]], dtype=torch.float32)
    # 使用上面搭建好的神经网络
    # 创建网络模型对象
    net = MLP()
    # 使用模型进行前向传播
    # net() 会自动的调用__call__(); 在__call__()内部调用的forward()
    pred = net(data)
    print(pred)

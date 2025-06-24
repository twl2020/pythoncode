import torch.nn as nn


def test01():
    # Linear: 线性的，在模型中就表示线性模型， 也就是 wx+b
    # out_features： 该线性层输出的特征数， 一个神经元输出一个特征
    # 所以 out_features的值 等于 该线性层上的神经元个数
    linear = nn.Linear(2, 3)
    # 使⽤从0-1均匀分布随机 初始化参数
    nn.init.uniform_(linear.weight)
    print(linear.weight)
    print("使⽤从0-1均匀分布随机", linear.weight.data)


def test02():
    # 创建Linear对象就已经对weight进行初始化了
    # 默认使用的是 kaiming初始化， 原因是目前在网络的中间层中使用比较多的激活函数是 relu激活函数
    # kaiming初始化是专门针对relu设计的
    # 权重初始化的作用是为了保证模型前向传播和反向传播的时候， 网络各层之间的方差保持相对一致。
    linear = nn.Linear(2, 3)
    print(linear.weight)
    # 使⽤固定值(常量) 初始化参数
    nn.init.constant_(linear.weight, 5)
    print("使⽤固定值(常量)", linear.weight)


if __name__ == '__main__':
    test02()

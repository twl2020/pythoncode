"""
MNIST训练集中有60000张图像， 如果直接将60000张图像一次性的交给模型，
模型压力很大， 可以无法训练， 此时我们应该将60000张数据分批次喂给模型。

如何将数据分批次？？ 使用DataLoader加载器

泛化能力： 指的就是模型在未知数据上的表现能力。   有点像生活中说的  举一反三的能力
"""
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

mnist_ds = datasets.MNIST(root="data", train=True, download=True,
                          transform=transforms.ToTensor())

# 使用DataLoader加载器对MNIST数据集进行分批次加载
# DataLoader合并了数据集、采样器， 是一个可迭代的对象
# batch_size: 表示批次的大小， 也就是每个批次有多少样本数据
# shuffle: 洗牌， 作用打乱数据, 以便提高模型的泛化能力
loader = DataLoader(mnist_ds, batch_size=100, shuffle=True)
print(loader)
print(len(loader))
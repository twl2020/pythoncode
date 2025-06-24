"""
该模块的主要是是划分数据集： 训练集和验证集
"""
from torch.utils.data import DataLoader, SubsetRandomSampler
from torchvision import datasets, transforms
import random


def get_tarin_valid(root="data", split_rate=0.2, batch_size=100):
    """
    获取验证集和测试集数据
    :param root: 加载数据集的路径
    :param split_rate: 划分训练集和验证集的比例
    :param batch_size: 每个批次的样本数量
    :return:
    """
    dataset = datasets.MNIST(root=root, train=True, download=True,
                             transform=transforms.ToTensor())

    print(dataset[0])

    # 构造出60000张图像的索引 0-59999
    length = len(dataset)
    indexs = list(range(length))
    random.seed(10)
    random.shuffle(indexs)
    # 将原始的索引打乱后采集20%的数据作为验证集
    split_rate = split_rate
    # 验证集的数量
    valid_num = int(length * split_rate)
    # 拆分出验证集和训练集的索引
    valid_dataset_index = indexs[:valid_num]
    tarin_dataset_index = indexs[valid_num:]

    # 创建采样器
    valid_sampler = SubsetRandomSampler(valid_dataset_index)
    train_sampler = SubsetRandomSampler(tarin_dataset_index)

    valid_loader = DataLoader(dataset=dataset, batch_size=batch_size, sampler=valid_sampler)
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, sampler=train_sampler)

    return train_loader, valid_loader


if __name__ == '__main__':
    get_tarin_valid("../data")
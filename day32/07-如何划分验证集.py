"""
划分验证集：
   从训练集中划分一部分数据作为验证集， 这里我们使用28比例

在pytorch中我们使用DataLoader加载数据喂给模型， DataLoader中有一个采样器sampler，
这个采样器就可以从训练集中采集部分数据作为验证集。

要使用采样器采集数据：
1. 需要创建采样器对象
2. 采样器采集数据的时候是根据索引采集的

"""
from torch.utils.data import DataLoader, SubsetRandomSampler
from torchvision import datasets, transforms
import random

dataset = datasets.MNIST(root="data", train=True, download=True,
                         transform=transforms.ToTensor())

# 构造出60000张图像的索引 0-59999
length = len(dataset)
indexs = list(range(length))
random.seed(10)
random.shuffle(indexs)
# 将原始的索引打乱后采集20%的数据作为验证集
split_rate = 0.2
# 验证集的数量
valid_num = int(length * split_rate)
# 拆分出验证集和训练集的索引
valid_dataset_index = indexs[:valid_num]
tarin_dataset_index = indexs[valid_num:]

# 创建采样器
valid_sampler = SubsetRandomSampler(valid_dataset_index)
train_sampler = SubsetRandomSampler(tarin_dataset_index)

valid_loader = DataLoader(dataset=dataset, batch_size=100, sampler=valid_sampler)
train_loader = DataLoader(dataset=dataset, batch_size=100, sampler=train_sampler)

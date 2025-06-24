from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import torch

cifar10_dataset = datasets.CIFAR10(root="data", train=True, download=True, transform=transforms.ToTensor())

loader = DataLoader(dataset=cifar10_dataset, batch_size=len(cifar10_dataset))

it = iter(loader)
imgages, _ = next(it)

# images的形状是： (50000, 3, 32, 32)

# 计算cifar10中样本数据的均值和标准差
# 计算的图像每个通道的均值和标准差
img_mean = torch.mean(imgages, dim=(0, 2, 3))
img_std = torch.std(imgages,  dim=(0, 2, 3))
print(img_mean)
print(img_std)


# 对cifar10的数据进行标准化的预处理
transforms.Compose([
    # 标准化处理
    transforms.Normalize(mean=img_mean, std=img_std)
])

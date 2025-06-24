"""
制作数据集的模块
"""
import numpy as np
import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import glob


class YellowDataset(Dataset):
    def __init__(self, root=None, transform=None):
        self.__img_paths = glob.glob(f"{root}/*")
        self.transform = transform
        pass

    def __len__(self):
        return len(self.__img_paths)

    def __getitem__(self, item):
        # 返回Image, label, loc
        img_path = self.__img_paths[item]
        # 加载图像
        img = Image.open(img_path)
        # 将图像转成Tensor
        img = self.transform(img)
        _, h, w = img.shape
        splits = img_path.split(".")
        label = torch.tensor(np.float32(splits[1:2]))
        loc = torch.tensor(np.float32(splits[2:6]))
        # loc数值比较大， 需要做缩放处理
        loc = loc / w
        return img, label, loc


if __name__ == '__main__':
    ds = YellowDataset("sample", transform=transforms.ToTensor())
    x = ds[1]
    print(x)

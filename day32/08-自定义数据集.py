"""
实际工作中，我们是不会训练内置数据集， 一般都是行业内收集的各种图像数据，
这些数据无法直接给模型， 需要先做成Dataset数据集， 然后使用数据加载器进行
加载。

自定义数据集必须继承 torch.utils.data 下的 Dataset类

自定义数据集  参照  MNIST


除了以下的代码实现数据集之外，还有一种相对更简单的方式： ImageFolder

ImageFolder加载图像的时候要注意， 是按照字节序加载的

0.png   1.png   2.png    3.png   10.png

0  1  10   2   3
"""
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os


class MyDataset(Dataset):

    def __init__(self, root=None, train=True, transform=None):
        self.__transform = transform
        self.__img_path = []
        self.__img_labels = []
        if train:
            # 加载训练集图像数据
            root_path = f"{root}/train"
        else:
            root_path = f"{root}/test"

        files = os.listdir(root_path)
        for file in files:
            file_path = os.path.join(root_path, file)
            img_files = os.listdir(file_path)
            for img_file in img_files:
                # 保存图像的路径和对应的分类标签
                self.__img_path.append(os.path.join(file_path, img_file))
                self.__img_labels.append(int(file))

    # MyDataset能够使用索引访问，需要重写__getitem__
    def __getitem__(self, index):
        # 根据索引返回 对应图像的Tensor和标签
        # 1. 获取图像路径加载图像
        img = Image.open(self.__img_path[index])
        if self.__transform is not None:
            # 2. 将图像转换成Tensor
            img = self.__transform(img)

        label = self.__img_labels[index]
        return img, label

    def __len__(self):
        return len(self.__img_labels)


if __name__ == '__main__':
    dataset = MyDataset(root="mnist", transform=transforms.ToTensor())
    print(len(dataset))
    img, label = dataset[0]
    # img.show()
    print(img)
    print(label)

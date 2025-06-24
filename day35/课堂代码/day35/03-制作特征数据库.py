"""
以图搜图的实现逻辑：
1.特征数据库， 里面存储了大量图像数据的特征信息
     这里我们使用txt文件表示特征数据库

     1.1 需要图像数据集
     1.2 使用已经训练好的模型， 提取图像数据集中的所有图像特征
     1.3 将提取到的图像特征存储在文件中
             文件中存储的数据信息：
                     图像1路径#[100, 10, 30, 34, 56, 28]
                     图像2路径#[11, 34, 200, 19, 30, 45]


2. 接收传入的图像，搜索最相似的5张图像
     2.1  使用已经训练好的模型， 提取传入的图像特征
     2.2  和特征数据库中的特征进行相似度比较 （欧式距离）
     2.3  将比较得到的距离进行升序
     2.4  取出前五张图像进行显示

"""
import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image
import glob


class Features:

    def __init__(self, img_root="imgs"):
        # 获取所有图像的路径地址
        self.img_paths = glob.glob(f"{img_root}/*")
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.CenterCrop(size=(224, 224))
        ])
        self.features = []

    def extract_feature(self):
        # 使用已经训练好的模型， 提取图像数据集中的所有图像特征
        net = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1)
        for img_path in self.img_paths:
            # 得到的时是 Image对象
            image = Image.open(img_path)
            # 将Image对象转成了FloatTensor, 形状是 CHW
            image_tensor = self.transform(image)
            # 将CHW 升维成 NCHW
            image_tensor = torch.unsqueeze(image_tensor, dim=0)
            # 将数据交给模型，提取特征
            # features = net(image_tensor)  # 直接调用forward， 得到的不是特征，而是全连接层输出的1000类别的分值
            # 以下的代码获取的才是图像的特征数据
            x = net.features(image_tensor)
            # Cannot use "squeeze" as batch-size can be 1
            x = nn.functional.adaptive_avg_pool2d(x, (1, 1))
            feature = torch.flatten(x, 1)
            # feature的形状是(n,v), feature[0]获取到的就是V
            self.features.append(feature[0])

    def save_imginfo_feature(self):
        # 提取所有图像的特征
        self.extract_feature()
        # 将图像的路径和对应的特征信息保存
        with open("img_features.txt", mode="w", encoding="UTF-8") as f:
            for i, imgpath in enumerate(self.img_paths):
                f.write(f"{imgpath}#{self.features[i].tolist()} \n")


if __name__ == '__main__':
    f = Features("imgs")
    f.save_imginfo_feature()

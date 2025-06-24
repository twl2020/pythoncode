"""
2. 接收传入的图像，搜索最相似的5张图像
     2.1  使用已经训练好的模型， 提取传入的图像特征
     2.2  和特征数据库中的特征进行相似度比较 （欧式距离）
     2.3  将比较得到的距离进行升序
     2.4  取出前五张图像进行显示
"""
from PIL import Image
from torch import nn
from torchvision import transforms, models
import torch
import json
import numpy as np


class SearchImage:

    def __init__(self):
        self.db_img_path = []
        self.db_features = []
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.CenterCrop(size=(224, 224))
        ])
        self.net = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.IMAGENET1K_V1)

    def __img_to_tensor(self, img_path):
        img = Image.open(img_path)
        img_tensor = self.transform(img)
        # 交给CNN需要的数据形状： NCHW
        img_tensor = torch.unsqueeze(img_tensor, dim=0)
        return img_tensor

    def __load_db_feature(self):
        with open("img_features.txt", mode="r", encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                splits = line.split("#")
                img_path = splits[0]
                img_feature = splits[1]
                self.db_img_path.append(img_path)
                # img_feature是字符串格式的特征向量 '[1,3,4,56,10,7,8]'
                # json.loads将json字符串转成python对象
                img_feature = json.loads(img_feature)
                self.db_features.append(img_feature)

    def __extract_feature(self, img_path):
        # 加载目标图像得到tensor
        img_tensor = self.__img_to_tensor(img_path)
        # 目标图像的特征
        x = self.net.features(img_tensor)
        # Cannot use "squeeze" as batch-size can be 1
        x = nn.functional.adaptive_avg_pool2d(x, (1, 1))
        # torch.flatten(x, 1)的形状是(n,v), [0]获取到的就是V
        target_feature = torch.flatten(x, 1)[0]
        return target_feature

    def search_img(self, img_path):
        distances = []
        # 获取特征数据库中的图像特征
        self.__load_db_feature()
        # 获取目标图像的特征
        target_feature = self.__extract_feature(img_path)
        # 使用目标图像的特征和数据库中的所有特征进行计算相似度
        for db_feature in self.db_features:
            distances.append(np.linalg.norm(target_feature.detach().numpy() - np.array(db_feature)))

        # 将distances进行按照索引升序
        idx = np.argsort(distances)[:5]
        # 根据idx加载imgpath
        img_paths = np.array(self.db_img_path)[idx]
        # 遍历路径加载图像
        for im_path in img_paths:
            Image.open(im_path).show()


if __name__ == '__main__':
    search = SearchImage()
    search.search_img("test02.jpeg")

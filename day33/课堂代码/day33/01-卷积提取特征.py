import torch
from PIL import Image
import torch.nn as nn
from torchvision import transforms
import matplotlib.pyplot as plt

img = Image.open("img/dog.jpg")
# (816, 597)
# print(img.size)
# 图像卷积操作使用Conv2d
# in_channels: 表示卷积层接收数据的通道数， 决定了卷积核的通道数
# out_channels: 表示的是输出特征图的通道数， 决定了卷积核的个数
# kernel_size: 表示的就是卷积核的大小
# (3, 816, 597)  ==> (4, 814, 595)
conv = nn.Conv2d(in_channels=3, out_channels=4, kernel_size=(11, 11))

# Conv2d卷积层需要接收的是 tensor, 所以需要将Image对象转Tensor
transform = transforms.ToTensor()
img_tensor = transform(img)

# (4, 814, 595)
feature_map = conv(img_tensor)
# 增加批次这个维度
feature_map = torch.unsqueeze(feature_map, 0)

# NCHW转成NHWC
feature_map = torch.permute(feature_map, (0, 2, 3, 1))

# 将tensor转成numpy数组， 以便显示数据
feature_array = feature_map.detach().numpy()
feature_array = feature_array[0]  # 取出第一个样本数据
plt.subplot(221).imshow(feature_array[:, :, 0])
plt.subplot(222).imshow(feature_array[:, :, 1])
plt.subplot(223).imshow(feature_array[:, :, 2])
plt.subplot(224).imshow(feature_array[:, :, 3])
plt.show()

"""
MNIST: 手写数字的图像
pytorch中内置了很多的数据集， 其中就包括MNIST数据集
"""
from torchvision import datasets, transforms

# root: 表示将数据集下载到哪个路径下, 会自动创建该路径
# train=True  表示加载的数据集是 训练集； False 表示加载的是 测试集
# download=True  表示目录下没有该数据集就会下载； 有了不会下载
# transforms.ToTensor()做了以下的操作：
# 1. 将PIL图像或者numpy数组转FloatTensor
# 2. 将HWC的形状转成CHW。(CUDA上使用CHW更加高效)
# 3. 将颜色范围从[0, 255]归一化到[0.0, 1.0]
mnist_ds = datasets.MNIST(root="data", train=True, download=True,
                          transform=transforms.ToTensor())

# mnist_ds存储了6000张训练集图像
"""
思考： img是pillow中的Image对象， 但是pytorch中网络模型接收的要求是 tensor,
所以需要将img转tensor， 如何转呢？？？
    就是加载数据集的时候使用transform进行转换
     
"""
img, label = mnist_ds[1]
img.show()
# print(label)

# print(mnist_ds.targets)
# print(mnist_ds.data)
# print(mnist_ds.classes)
# print(mnist_ds.class_to_idx)

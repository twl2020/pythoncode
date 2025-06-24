import cv2
import numpy as np
from PIL import Image

# opencv无法处理中文， 所以文件路径或名称不能右中文
# 读取图像, 返回的是该图像对应的numpy数组
# opencv中图像形状默认是 HWC
img = cv2.imread("c.jpeg")
# print(type(img))  # <class 'numpy.ndarray'>

# 验证， opencv的颜色通道默认是 BGR
# 使用切片将每个通道获取出来
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

# 将以上的通道按照rgb组合并显示
img_new = np.stack((r, g, b), axis=2)
img01 = Image.fromarray(img_new)
img01.show()


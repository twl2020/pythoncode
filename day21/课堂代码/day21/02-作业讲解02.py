"""
给图像添加边框
思路：
    1. 加载图像
    2. 转成numpy数组
    3. 为所欲为
"""
from PIL import Image
import numpy as np

img = Image.open("c.jpeg")

# 转numpy数组
img_arr = np.array(img)
# 使用切片的方式给图像添加边框
img_arr[:, :50] = [0, 0, 255]  # 左边的边框
img_arr[:50] = [0, 0, 255]  # 上边的边框
img_arr[:, -50:] = [255, 0, 0]  # 右边的边框
img_arr[-50:] = [255, 0, 0]  # 下边的边框

# 将数组转成Image
img01 = Image.fromarray(img_arr)
img01.show()

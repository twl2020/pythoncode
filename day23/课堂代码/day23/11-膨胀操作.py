import cv2
import numpy as np

bg = np.zeros((10, 10), "u1")
bg[3:7, 3:7] = 255

# 创建一个结构元素
# 第一个参数表示： 结构元素的形状
# 第二个参数： 结构元素的尺寸
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(kernel)
"""
膨胀操作：
当结构元素在图像集合上移动时：
1. 结构元素和图像有交集的时候， 就将结构元素中心点对应的图像像素改成255
2. 结构元素和图像没有有交集的时候， 就将结构元素中心点对应的图像像素就是0
"""
dilate_img = cv2.dilate(bg, kernel)

print(bg)

import cv2
import numpy as np

bg = np.zeros((10, 10), "u1")
bg[3:7, 3:7] = 255

# 创建一个结构元素
# 第一个参数表示： 结果元素的形状

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

print(kernel)

# 腐蚀
"""
结构元素在原图上移动：
1. 当结构元素不全部属于图像集合的时候，结构元素中心点对应的图像集合的像素点变成0
2. 当结构元素全部属于图像集合的时候，结构元素中心点对应的图像集合的像素点不变
"""
erode_img = cv2.erode(bg, kernel)

print(bg)

"""
获取HSV颜色范围


获取黄色的hsv
"""

import cv2
import numpy as np

# 用数组表示yellow一个像素点
yellow = np.uint8([[[0, 255, 255]]])

# print(yellow.shape) # (1, 1, 3)

# 将BGR转HSV
yellow_hsv_img = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
# 计算yellow的hsv范围
# [H-10,100,100]和[H+10,255, 255]分别作为下界和上界
yellow_hsv_low = (yellow_hsv_img[0, 0, 0] - 10, 100, 100)
yellow_hsv_up = (yellow_hsv_img[0, 0, 0] + 10, 255, 255)

print(yellow_hsv_low)
print(yellow_hsv_up)
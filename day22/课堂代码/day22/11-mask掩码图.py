"""
mask掩码图：
   mask可以想象生活中的 面膜， 我们可以看见眼睛， 其余被遮挡的部分就看不见了

1. mask掩码图像是一个单通道黑白图像
2. 白色表示我们感兴趣的内容； 黑色表示不感兴趣的

作用： 使用mask可以获取到图像的 ROI
"""

import cv2
import numpy as np

img = cv2.imread("mn.jpeg")
h, w, _ = img.shape

# 制作掩码图
mask = np.zeros((h, w), "u1")

# 在mask上画一个圆， 作为感兴趣的区域 ROI
cv2.circle(mask, (200, 200), 100, (255, 255, 255), -1, cv2.LINE_AA)

# 将掩码图和原图做位运算得到原图的ROI
dst = cv2.bitwise_and(img, img, mask=mask)


cv2.imshow("win", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

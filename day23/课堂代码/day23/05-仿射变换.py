"""
仿射变换：在仿射变换中，原始图像中的所有平行线在输出图像中仍将平行。
为了找到变换矩阵，我们需要输入图像中的三个点及其在输出图像中的对应位置。
然后cv2.getAffineTransform将创建一个2x3矩阵，该矩阵将传递给cv2.warpAffine。

"""

import cv2
import numpy as np

img = cv2.imread("hmg.jpeg")
h, w, _ = img.shape

# 获取仿射变换的 变换矩阵
src = np.float32([[0, 0], [600, 10], [10, 800]])
dst = np.float32([[100, 210], [700, 120], [100, 1000]])

m = cv2.getAffineTransform(src, dst)

dst_img = cv2.warpAffine(img, m, (w, h))

cv2.imshow("win", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
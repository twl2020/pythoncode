"""
透视变换：对于透视变换，需要3x3变换矩阵。即使在转换后，直线也将保持直线。
要找到此变换矩阵，您需要在输入图像上有4个点，在输出图像上需要相应的点。
在这四个点中，其中三个不应共线。然后可以通过函数cv2.getPerspectiveTransform找到变换矩阵。
然后将cv2.warpPerspective应用于此3x3转换矩阵。

"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("zy.jpeg")
h, w, _ = img.shape

# 使用matplotlib显示图像
# plt.imshow(img)
# plt.show()

src = np.float32([
    [0, 160],
    [600, 160],
    [180, 1250],
    [900, 1250]
])

dst = np.float32([
    [0, 0],
    [1080, 0],
    [0, 1439],
    [1080, 1439]
])

# 获取透视变换的矩阵
m = cv2.getPerspectiveTransform(src, dst)
dst_img = cv2.warpPerspective(img, m, (w, h))
cv2.imshow("win", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
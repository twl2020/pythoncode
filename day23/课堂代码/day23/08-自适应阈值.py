"""
cv2.adaptiveThreshold():  除全局阈值的参数外，该方法还包含三个输入参数：
adaptiveMethod决定阈值是如何计算的：
    cv.ADAPTIVE_THRESH_MEAN_C  阈值是邻近区域的平均值减去常数C
    cv.ADAPTIVE_THRESH_GAUSSIAN_C  阈值是邻域值的高斯加权总和减去常数C
BLOCKSIZE：确定附近区域的大小
C 是从邻域像素的平均或加权总和中减去的一个常数
"""

import cv2

img = cv2.imread("hmg.jpeg")
# 将原始图像进行阈值处理， 得到二值图像
# 1. 先将原始图像转灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2. 使用自适应阈值进行阈值处理, 返回值： (阈值， 二值图像)
dst_img = cv2.adaptiveThreshold(img_gray, 255,
                                cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 10)

cv2.imshow("win", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
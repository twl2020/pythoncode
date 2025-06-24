"""
简单阈值(全局阈值): 对于每个像素，应用相同的阈值。如果像素值小于阈值，则将其设置为0，否则将其设置为最大值(一般设置成255)。
cv2.threshold()：用于简单阈值。
第一个参数是源图像，它应该是灰度图像。
第二个参数是阈值，用于对像素值进行分类。
第三个参数是分配给超过阈值的像素值的最大值。
OpenCV提供了不同类型的阈值，这由函数的第四个参数给出。
该方法返回两个输出。第一个是使用的阈值，第二个输出是阈值后的图像。
"""

import cv2

img = cv2.imread("hmg.jpeg")
# 将原始图像进行阈值处理， 得到二值图像
# 1. 先将原始图像转灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2. 进行阈值处理, 返回值： (阈值， 二值图像)
# _, dst_img = cv2.threshold(img_gray, 180, 255, cv2.THRESH_BINARY)
"""
THRESH_OTSU: 使用"大津算法" 自动计算阈值, 此时参数thresh是没有意义
"""
_, dst_img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
cv2.imshow("win", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

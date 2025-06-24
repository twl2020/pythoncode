"""
直角矩形(最大外接矩形)：不考虑物体的旋转。所以直角矩形的面积不是最小的。
它是由函数cv.boundingRect()找到的。

"""

import cv2

img = cv2.imread("xx.png")

# 绘制最大外接矩形
# 1. 获取图像的轮廓
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
# contours中存储的就是所有轮廓， 每个轮廓所有点位的坐标
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

box = cv2.boundingRect(contours[0])
# 得到绘制矩形的左上角坐标和矩形的宽高
x, y, w, h = box
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

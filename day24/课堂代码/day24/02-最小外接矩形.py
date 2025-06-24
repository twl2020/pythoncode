"""
旋转矩形(最小外接矩形)：是用最小面积绘制的，所以它也考虑了旋转。
使用的函数是cv.minAreaRect()。它返回一个Box2D结构，
其中包含以下细节 -(中心(x,y)，(宽度，高度)，旋转角度)。
但要画出这个矩形，我们需要矩形的四个角。它由函数cv.boxPoints()获得


绘制最小外接矩形的步骤：
1. 获取图像的轮廓
2. 传入轮廓的得到最小外接矩形  -- box = minAreaRect(contours[index])
3. 获取最小外接矩形的四个角坐标 -- points = boxPoints(box)
4. 使用绘制轮廓的方法绘制最小外接矩形
    a， points必须升维成3维
    b. points中的元素必须是int32或int64的数据类型
"""
import cv2
import numpy as np

img = cv2.imread("xx.png")

# 绘制最小外接矩形
# 1. 获取图像的轮廓
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
# contours中存储的就是所有轮廓， 每个轮廓所有点位的坐标
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# 将轮廓交给minAreaRect函数，得到最小外接矩形
# 返回的是： (中心(x,y)，(宽度，高度)，旋转角度)
box = cv2.minAreaRect(contours[0])
# 获取最小外接矩形 box的四个角的坐标
points = cv2.boxPoints(box)
print(points)

# 因为这里的矩形是四个角的坐标，不能使用之前绘制矩形的方法； 应该使用 绘制轮廓的方法
# 绘制轮廓的时候，contours必须是三维的， points是二维的， 所以需要升维
# 绘制轮廓的时候，contours的坐标必须是整数(int32， int64)， points是浮点数
# intp函数将数据变成int64
points = np.int32(points)
cv2.drawContours(img, [points], -1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

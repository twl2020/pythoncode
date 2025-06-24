import cv2
import numpy as np

# 准备一个黑色的背景
bg = np.zeros((480, 640, 3))

# 画线
# 参数1： 表示在哪个图像上绘制
# 参数2： 表示线段的第一个点
# 参数3： 表示线段的第二个点
# 参数4： 颜色（BGR）
# 参数5： 线宽
# 参数6： 线条类型  LINE_4   LINE_8   LINE_AA 值越大，线条抗锯齿效果越好
cv2.line(bg, (10, 10), (400, 400), (0, 0, 255), 3, cv2.LINE_AA)

# 绘制矩形
# pt1: 左上角的左边
# pt2: 右上角的左边
cv2.rectangle(bg, (10, 10), (300, 300), (255, 255, 0), 3, cv2.LINE_AA)
# 绘制实心矩形
# thickness=-1  表示实心
cv2.rectangle(bg, (50, 50), (200, 200), (0, 255, 255), -1, cv2.LINE_AA)
# 绘制圆
# center: 圆心坐标
# radius: 半径
cv2.circle(bg, (100, 100), 50, (255, 0, 0), -1, cv2.LINE_AA)
# 绘制椭圆
# center: 绘制的圆心坐标
# axes: 椭圆的主轴半径
# angle: 椭圆旋转角度
# startangle: 椭圆起始角度
# endangle: 椭圆结束角度
# cv2.ellipse(bg, (200, 200), (100, 50), 0, 0, 360, (0, 255, 0), 3, cv2.LINE_AA)
cv2.ellipse(bg, (200, 200), (100, 50),
            60, 0, 180, (0, 255, 0), -1, cv2.LINE_AA)
cv2.imshow("win", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
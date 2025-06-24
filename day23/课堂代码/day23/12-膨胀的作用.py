"""
效果： 扩大图像中的物体
"""
import cv2

img = cv2.imread("e.png")

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 膨胀操作
img01 = cv2.dilate(img, kernel, iterations=3)

cv2.imshow("win", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()


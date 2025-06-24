"""
为了找到此转换矩阵，OpenCV提供了一个函数cv2.getRotationMatrix2D(center, angle, scale)

"""
import cv2

img = cv2.imread("hmg.jpeg")
h, w, _ = img.shape

# 获取旋转和缩放的 变换矩阵
m = cv2.getRotationMatrix2D((0, 0), 10, 0.2)

dst_img = cv2.warpAffine(img, m, (w, h))

cv2.imshow("win", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
opencv图像的颜色空间是： BGR
"""
import cv2

img = cv2.imread("mn.jpeg")

# 将 BGR --> RGB
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("win", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
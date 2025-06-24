import cv2
import numpy as np

# img = cv2.imread("e.png")
img = cv2.imread("m01.jpg")

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
print(kernel)
# 腐蚀操作
# iterations: 腐蚀次数
erode_img = cv2.erode(img, kernel, iterations=3)

result = np.hstack((img, erode_img))

cv2.imshow("win", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

img = cv2.imread("i1.png")

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 形态学梯度
img01 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("win", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()
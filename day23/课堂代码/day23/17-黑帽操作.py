import cv2

img = cv2.imread("x2.jpg")

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 形态学黑帽
img01 = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=5)

cv2.imshow("win", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()
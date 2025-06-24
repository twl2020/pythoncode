import cv2

img = cv2.imread("mn.jpeg")

# 拆分通道
b, g, r = cv2.split(img)

# 合并通道
img01 = cv2.merge((b, g, r))

cv2.imshow("win", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img = cv2.imread("hmg.jpeg")

# 图像的缩放
img01 = cv2.resize(img, (200, 200))
print(img.shape)
print(img01.shape)

# 图像旋转
img02 = cv2.rotate(img01, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("win", img02)
cv2.waitKey(0)
cv2.destroyAllWindows()
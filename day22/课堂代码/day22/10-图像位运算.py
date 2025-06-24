import cv2

img01 = cv2.imread("m01.png")
img02 = cv2.imread("m02.png")
img02 = cv2.resize(img02, (570, 812))

# 图像按位与
# img03 = cv2.bitwise_and(img01, img02)
# 图像按位或
# img03 = cv2.bitwise_or(img01, img02)
# 图像按位异或
# img03 = cv2.bitwise_xor(img01, img02)
# 图像按位取反
img03 = cv2.bitwise_not(img01)
cv2.imshow("win", img03)
cv2.waitKey(0)
cv2.destroyAllWindows()
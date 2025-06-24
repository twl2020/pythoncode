"""
平移：平移是物体位置的移动。如果您知道在(x,y)方向上的位移，则将其设为(tx,ty)，
你可以创建转换矩阵M，如下所示：
   [[1, 0, dx],
    [0, 1, dy]]

cv2.warpAffine()函数的第三个参数是输出图像的大小，其形式应为(width，height)。记住width =列数，height =行数。
转换矩阵的元素类型必须是float32或float64

"""
import cv2
import numpy as np

img = cv2.imread("hmg.jpeg")
h, w, _ = img.shape

# 创建平移矩阵
m = np.float32([
    [1, 0, 10],
    [0, 1, 50]
])

# w+10 是平移后新图像的宽度， +10是为了完全显示出平移后图像宽度
dst_img = cv2.warpAffine(img, m, (w+10, h+50))

cv2.imshow("win", dst_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
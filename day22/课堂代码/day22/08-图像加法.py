import cv2

"""
cv.add()或通过numpy操作res = img1 + img2添加两个图像。两个图像应具有相同的深度和类型，或者第二个图像可以只是一个标量值。

图像融合：
addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None) ：这也是图像加法，但是对图像赋予不同的权重，以使其具有融合或透明的感觉

"""
m1 = cv2.imread("mn.jpeg")
m2 = cv2.imread("st.jpeg")

m1 = cv2.resize(m1, (500, 500))
m2 = cv2.resize(m2, (500, 500))

# 图像做运算： 必须有相同的尺寸和通道数
# m3 = cv2.add(m1, m2)
# 图像融合
m3 = cv2.addWeighted(m1, 0.3, m2, 0.8, -100)
cv2.imshow("win", m3)
cv2.waitKey(0)
cv2.destroyAllWindows()

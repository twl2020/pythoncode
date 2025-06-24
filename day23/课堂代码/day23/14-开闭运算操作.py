"""
开运算：
效果： 断开较窄的粘连线，消除较细的突出物和噪音，使图像的轮廓变得光滑
先腐蚀，然后再膨胀

效果： 关闭前景对象内部的小孔或对象上的小黑点时很有用。使图像的轮廓变得光滑
先膨胀，然后再腐蚀
"""

import cv2

img = cv2.imread("x1.jpg") # 开运算使用的图像
# img = cv2.imread("x2.jpg")  # 闭运算使用的图像

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 开运算
img01 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=3)
# 闭运算
# img01 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)

cv2.imshow("win", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()

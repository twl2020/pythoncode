"""
开运算：
效果： 断开较窄的粘连线，消除较细的突出物和噪音，使图像的轮廓变得光滑
先腐蚀，然后再膨胀

效果： 关闭前景对象内部的小孔或对象上的小黑点时很有用。使图像的轮廓变得光滑
先膨胀，然后再腐蚀
"""

import cv2

img = cv2.imread("e.png")

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# # 先腐蚀
# erode_img = cv2.erode(img, kernel, iterations=3)
# # 再膨胀
# dilate_img = cv2.dilate(erode_img, kernel, iterations=3)

# 开运算
# img01 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=3)
# 闭运算
img01 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)


cv2.imshow("win", img01)
cv2.waitKey(0)
cv2.destroyAllWindows()

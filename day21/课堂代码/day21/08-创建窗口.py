import cv2

img = cv2.imread("c.jpeg")
# 创建窗口, 定义窗口
# WINDOW_NORMAL: 可以修改窗口大小
# WINDOW_AUTOSIZE： 根据显示内容自动判断窗口大小， 不能手动调整大小
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow("win", 300, 200)
cv2.imshow("win", img)
cv2.waitKey(0)

# 保存图像
cv2.imwrite("www.png", img)
cv2.destroyAllWindows()
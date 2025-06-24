import cv2

img = cv2.imread("c.jpeg")

# 显示图像
# 参数一： 显示图像的窗口名称， 如果该窗口实现没有创建， 那么这里会自动创建
# 如果事先创建了该窗口， 就使用创建好的窗口
# 参数二： 需要显示的图像
cv2.imshow("win", img)

# delay： 0表示永远， 也就是一直等待， 直到按下按键
# delay>0 表示等待的毫秒数
# 返回按键对应数值， esc按键对应 27
code = cv2.waitKey(0)
print(code)
# print(ord("q"))

# 最后一步： 释放窗口
# cv2.destroyWindow("win")
cv2.destroyAllWindows()

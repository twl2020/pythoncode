"""
将图像fans.jpg 添加到b.jpeg上。
要求： 使用opencv代码去除fans.jpg的白色背景
"""
import cv2

bg = cv2.imread("resources/b.jpeg")
fans = cv2.imread("resources/fans.jpg")
h, w, _ = fans.shape
# 对粉丝牌图像进行尺寸调整
fans = cv2.resize(fans, (w // 4, h // 4))

# 1. 查找粉丝牌的轮廓，得到白底黑色物体的掩码图mask01
fans_gray = cv2.cvtColor(fans, cv2.COLOR_BGR2GRAY)
_, fans_mask01 = cv2.threshold(fans_gray, 0, 255, cv2.THRESH_OTSU)
contours, _ = cv2.findContours(fans_mask01, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(fans_mask01, contours, 1, (0, 0, 0), -1, cv2.LINE_AA)

# 2. 然后得到 黑底白色物体的掩码图mask02
fans_mask02 = cv2.bitwise_not(fans_mask01)

# 3. 截取roi区域
fan_h, fan_w, _ = fans.shape
roi = bg[50: 50 + fan_h, 100: 100 + fan_w]

# 4. 将fans_mask02和fans图像进行按位与
fans_black = cv2.bitwise_and(fans, fans, mask=fans_mask02)

# 5. 将fans_mask01和roi图像进行按位与
roi_black = cv2.bitwise_and(roi, roi, mask=fans_mask01)

# 6. 将fans_black 和 roi_black 进行按位或
roi_result = cv2.bitwise_or(fans_black, roi_black)

# 7. 将roi_result放回原图
bg[50: 50 + fan_h, 100: 100 + fan_w] = roi_result
cv2.imshow("win", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

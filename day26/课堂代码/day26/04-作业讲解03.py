"""
3. 使用OpenCV完成图中药丸数量的统计

分析：
1， 腐蚀 -- 分开药丸
2， 查找轮廓 -- 轮廓的数量就是药丸的数量
"""
import cv2
img = cv2.imread("resources/yaowan.jpg")

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
erod_img = cv2.erode(img_bin, kernel, iterations=4)
# 查找轮廓
contours, _ = cv2.findContours(erod_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)
print(len(contours))
cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
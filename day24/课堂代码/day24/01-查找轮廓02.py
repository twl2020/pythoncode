import cv2

img = cv2.imread("t3.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

# 查找轮廓
"""
cv2.RETR_LIST: 查找的是所有轮廓， 但是只返回轮廓的顺序关系， 不返回嵌套关系， 也就是next和previous有值； 
first_child 和 parent 都是 -1
"""
# contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
"""
cv2.RETR_CCOMP: 查找的是所有轮廓，将所有的轮廓组织成2层层级关系（外层轮廓和内层轮廓）
外层轮廓： first_child != -1， parent = -1
内层轮廓： first_child = -1， parent != -1
"""
# contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
"""
cv2.RETR_TREE: 查找的是所有轮廓, 组织了所有轮廓的层级关系，
也就是next , previous, first_child, parent都有值

"""
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print(hierarchy.shape)
print(hierarchy)
# for i, contour in enumerate(contours):
#     if hierarchy[0][i][3] == -1:  # 外层轮廓
#         cv2.drawContours(img, contours, i, (0, 0, 255), 2, cv2.LINE_AA)
#     else:
#         cv2.drawContours(img, contours, i, (255, 0, 0), 2, cv2.LINE_AA)

cv2.drawContours(img, contours, 3, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
图像轮廓是具有相同颜色或灰度的连续点的曲线

findContours(image, mode, method[, contours[, hierarchy[, offset]]]) -> contours, hierarchy

RETR_EXTERNAL = 0 这是最简单的检索模式，只检索最外层的轮廓，即不包括任何嵌套轮廓。如果你只关心物体的外部边界，而不考虑其内部结构或孔洞，这个模式就很适用。
RETR_LIST = 1 该模式检索所有轮廓，并将其作为列表返回，但不创建任何层次结构。每个轮廓都是独立的，没有父子关系信息。适用于需要所有轮廓但不需要它们之间关系的场景。
RETR_CCOMP = 2在这种模式下，检索到的轮廓被组织成两层层次结构。顶层是外部边界，第二层是孔和内部边界。如果一个对象内有多个孔，则孔被视为同一层级。这对于需要区分外边界和内部孔洞的场景很有用。
RETR_TREE = 3 这是最复杂的检索模式，构建了一个完整的轮廓层次树。每个轮廓都有一个层次信息，可以区分出父轮廓和子轮廓（内部轮廓），非常适合于需要分析复杂结构和多级嵌套轮廓的场景。


Method:
CHAIN_APPROX_NONE = 1:  轮廓中的每一点都会被精确保存下来
CHAIN_APPROX_SIMPLE = 2: 仅保留轮廓的端点和具有拐角的点来简化轮廓表示


drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) -> image
Image 要绘制的轮廓图像
Contours 轮廓点
contourIdx 要绘制的轮廓编号， -1表示绘制所有轮廓
Color: 轮廓的颜色
Thickness: 线宽， -1表示填充

"""
import cv2

img = cv2.imread("x3.jpg")

img_gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
hierarchy表示轮廓的层级， 形状是(1, 轮廓数量, 4)
hierarchy中的元素的 [next, previous, first_child, parent]
以上元素的值如果是-1， 表示没有对应的轮廓
next： 下一个轮廓的索引
previous： 前一个轮廓的索引
first_child： 第一子轮廓的索引
parent： 父轮廓的索引

cv2.RETR_EXTERNAL: 获取的是做外层的轮廓， 不包括任何嵌套轮廓  [[[-1, -1,-1,-1]]]

"""
# contours, hierarchy = cv2.findContours(img_gary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(img_gary, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(hierarchy)
# 第三个参数表示轮廓的索引， 也就是需要绘制哪一个轮廓， 0表示第一个轮廓； -1表示所有轮廓
cv2.drawContours(img, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

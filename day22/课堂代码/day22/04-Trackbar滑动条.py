"""
Trackbar滑动条
createTrackbar(trackbarName, windowName, value, count, onChange) -> None  创建滑动条
第一个参数是轨迹栏名称，
第二个参数是它附加到的窗口名称，
第三个参数是默认值，
第四个参数是最大值，第五个是执行的回调函数每次跟踪栏值更改
回调函数始终具有默认参数，即轨迹栏位置

getTrackbarPos(trackbarname, winname) -> retval  获取滑动条的值。

案例效果： 调色板
"""
import cv2
import numpy as np


def bar_change(pos):
    """
    滑动条的回调将函数
    :param pos: 就是接收滑动条上面的数值
    :return:
    """
    # 在监听事件的回调函数中获取多个滑动条上的结果， 前提是： 多个滑动条的初始值是0
    r = cv2.getTrackbarPos("R", "win")
    g = cv2.getTrackbarPos("G", "win")
    b = cv2.getTrackbarPos("B", "win")
    bg[:, :] = [b, g, r]


bg = np.zeros((480, 640, 3), "u1")
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", 640, 480)
# onChange: 表示是滑动条改变的事件， 接收一个回调函数， 当改变事件触发的时候自动调用该回调函数实现功能
cv2.createTrackbar("R", "win", 0, 255, bar_change)
cv2.createTrackbar("G", "win", 0, 255, bar_change)
cv2.createTrackbar("B", "win", 0, 255, bar_change)

while True:
    cv2.imshow("win", bg)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

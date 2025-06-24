"""
鼠标事件： 就是在opencv中可以监听到鼠标的按下，松开， 滑动等操作
cv2. setMouseCallback(windowName, onMouse, param=None)
第一个参数： 窗口名称
第二个参数： 鼠标回调函数，该函数在发生鼠标事件时执行
第三个参数： 传递给回调函数的参数

回调函数： 回调函数是程序员定义的，但是不是程序员调用的
回调函数是程序达到某个条件后自动调用的。

回调函数：创建鼠标回调函数具有特定的格式
def 函数名(event,x,y,flags,param):

"""

import cv2
import numpy as np


def mouse_callback(event, x, y, flags, params):
    """
    鼠标事件的回调函数
    :param event: 事件类型
    :param x: 鼠标在窗口上的坐标
    :param y: 鼠标在窗口上的坐标
    :param flags: 组合键的类型
    :param params: 参数, 接收的是setMouseCallback()中的param
    :return:
    """
    if event == cv2.EVENT_LBUTTONDOWN:  # 鼠标左键按下
        global x0, y0
        x0, y0 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        # 绘制线条
        cv2.line(bg, (x0, y0), (x, y), (0, 0, 255), 3, cv2.LINE_AA)

    elif event == cv2.EVENT_MOUSEMOVE:
        pass
    cv2.imshow("win", bg)


cv2.namedWindow("win", cv2.WINDOW_AUTOSIZE)

# 准备一个黑色的背景
bg = np.zeros((480, 640, 3), "u1")

# onMouse就是接收回调函数的
cv2.setMouseCallback("win", mouse_callback)

cv2.imshow("win", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

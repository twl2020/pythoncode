"""
要捕获视频，你需要创建一个 VideoCapture 对象。它的参数可以是设备索引或视频文件的名称。
设备索引就是指定哪个摄像头的数字。正常情况下，一个摄像头会被连接。所以可以简单地传0(或-1)。
你可以通过传递1来选择第二个相机，以此类推。在此之后，你可以逐帧捕获。

但是在最后，不要忘记释放资源。


视频 = 一帧一帧的图像
"""

import cv2
# 0表示的是设备索引号，也就是第一个摄像头
cap = cv2.VideoCapture(0)
# print(cap.isOpened())
# 从摄像头中读取图像
while cap.isOpened():
    # read: 读取视频帧， 返回两个值： 是否读取成功， 读取到的图像
    ret, img = cap.read()
    if not ret:
        break
    cv2.imshow("win", img)
    # 以下代码表示等待25毫秒读取一帧图像
    code = cv2.waitKey(25)
    # 表示按下esc键的时候退出循环
    if code == 27:
        break

cap.release()  # 释放摄像头资源
cv2.destroyAllWindows()
"""
背景分离方法: 主要用用在视频中
视频中前景： 表示的动态的物体 -- 会动的
视频中背景： 表示静态的物体 -- 不会动的

背景分离方法： 就是去除不会动的物体

背景分离需要使用背景减除器

"""

import cv2
cap = cv2.VideoCapture(0)

# 创建背景减除器对象
bg_sub = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 将frame做成灰度图像， 使用的时候大家需要测试 灰度图和二值图哪一个效果好就用哪个
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 使用背景减除器处理视频中的每一帧画面
    mask = bg_sub.apply(frame_gray)
    cv2.imshow("frame", mask)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()
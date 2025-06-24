import cv2

# 传入视频文件的路径
cap = cv2.VideoCapture("D://xx.mp4")
# 获取视频的宽高
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 设置窗口并调整大小
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", int(w // 4), int(h // 4))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("win", frame)
    if cv2.waitKey(25) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
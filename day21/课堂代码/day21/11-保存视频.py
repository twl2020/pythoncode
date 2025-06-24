import cv2


cap = cv2.VideoCapture("D://xx.mp4")
# 获取视频的宽高
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 设置窗口并调整大小
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", int(w // 4), int(h // 4))

# 保存使用需要是 VideoWriter对象
# fourcc: four character code 每种视频类型都有四字符编码 "m" "p" "4" "v"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# 注意： 保存视频的时候， 视频的宽高必须和原始视一致
out = cv2.VideoWriter("yy.mp4", fourcc, 25, (int(w), int(h)))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("win", frame)
    # 保存
    out.write(frame)
    if cv2.waitKey(25) == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
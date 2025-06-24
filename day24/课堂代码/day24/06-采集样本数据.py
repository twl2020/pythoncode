import cv2

cap = cv2.VideoCapture(0)
count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    code = cv2.waitKey(25)
    if code == 27:
        break
    elif code == ord("s"):
        # 保存当前帧
        cv2.imwrite(f"data/0/{count}.png", frame)
        count += 1

cap.release()
cv2.destroyAllWindows()

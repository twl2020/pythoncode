import cv2
import numpy as np
from PIL import Image


def get_yellow_hsv():
    # 用数组表示yellow一个像素点
    yellow = np.uint8([[[0, 255, 255]]])
    # 将BGR转HSV
    yellow_hsv_img = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
    # 计算yellow的hsv范围
    # [H-10,100,100]和[H+10,255, 255]分别作为下界和上界
    yellow_hsv_low = (yellow_hsv_img[0, 0, 0] - 10, 100, 100)
    yellow_hsv_up = (yellow_hsv_img[0, 0, 0] + 10, 255, 255)
    # 返回yellow颜色 hsv的上界和下界
    return np.uint8(yellow_hsv_low), np.uint8(yellow_hsv_up)


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    low, up = get_yellow_hsv()
    # 将farme转hsv
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame_hsv, low, up)
    mask_img = Image.fromarray(mask)
    box = mask_img.getbbox()
    if box is not None:
        lx, ly, rx, ry = box
        cv2.rectangle(frame, (lx, ly), (rx, ry), (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("win", frame)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()

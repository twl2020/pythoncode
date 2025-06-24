import cv2
import numpy as np
from PIL import Image

"""
1. 计算yellow的hsv范围
2. 制作掩码图
3. 获取yellow的边框坐标
4. 绘制边框

"""
img = cv2.imread("m.jpg")


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


# 制作掩码图
low, up = get_yellow_hsv()

# 将img转hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img_hsv, low, up)

# 将mask转成Image
mask_img = Image.fromarray(mask)
# getbbox(): 获取非0区域的边界坐标， 左上角和右下角的坐标
box = mask_img.getbbox()
if box is not None:
    lx, ly, rx, ry = box
    # 在原图上绘制矩形
    cv2.rectangle(img, (lx, ly), (rx, ry), (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

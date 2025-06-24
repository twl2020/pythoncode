import cv2
import numpy as np


# 函数需要遵循： 单一职责
def hsv_red_mask(img):
    """
    获取图像红色的hsv对应的掩码图
    :param img: 传入的原始图像
    :return: 掩码图
    """
    # 定义低值区红色的hsv范围
    low01 = np.uint8([0, 43, 46])
    up01 = np.uint8([10, 255, 255])
    # 定义高值区红色的hsv范围
    low02 = np.uint8([156, 43, 46])
    up02 = np.uint8([180, 255, 255])
    # 将原图img的色彩空间修改成hsv
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 获取低值区在原图中的掩码图
    mask01 = cv2.inRange(img, low01, up01)
    # 获取高值区在原图中的掩码图
    mask02 = cv2.inRange(img, low02, up02)
    # 将mask01和mask02做按位或运算(并集)得到最终的掩码图mask
    mask = cv2.bitwise_or(mask01, mask02)
    return mask


if __name__ == '__main__':
    # 加载原图
    img = cv2.imread("hmg.jpeg")
    # 得到掩码图
    mask = hsv_red_mask(img)

    # 抠图得到红色的玫瑰花  -- 按位与操作
    flower = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("win", flower)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

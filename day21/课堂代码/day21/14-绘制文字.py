import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 准备一个黑色的背景
bg = np.zeros((480, 640, 3), "u1")

# 绘制文字  -- OpenCV不能处理中文
# org: 文字左下角的坐标
# fontFace： 字体的样式
# fontScale: 字体大小缩放因子
cv2.putText(bg, "I Love You", (100, 100),
            cv2.FONT_ITALIC, 2, (0, 0, 255), 3, cv2.LINE_AA)


# 绘制中文使用pillow
img = Image.fromarray(bg)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("simhei.ttf", 70)

draw.text((250, 250), "我爱你", (0, 0, 255), font)

# 将Image图像转成numpy数组
bg = np.array(img)

cv2.imshow("win", bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

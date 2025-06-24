# 导入Image模块
from PIL import Image

# 方式1： 从文件对象中加载图像
with open("b.jpeg", mode="rb") as f:
    # mode的值必须是r, 默认就是r
    image = Image.open(f, mode="r")
    # show() 调用系统中内置的看图软件显示图像
    # image.show()

# 方式2： 从文件中加载图像
# im = Image.open("b.jpeg")
# im.show()

# 方式3: 从头创建图像
# mode: 表示的是创建出来的图像的模式 （灰度图， 彩色图）
# Pillow不支持每通道深度超过8位的多通道图像。
# size = (宽, 高)
# img = Image.new(mode="RGB", size=(480, 640), color=(255, 0, 0))
img = Image.new(mode="L", size=(480, 640), color=127)
img.show()
# print(img)


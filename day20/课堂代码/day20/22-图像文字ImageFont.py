"""
ImageFont模块定义了一个同名的类。该类的实例存储位图字体，并与PIL.ImageDraw.ImageDraw.text()方法一起使用。
PIL使用自己的字体文件格式来存储位图字体，限制为256个字符。
从1.1.4版开始，PIL可以配置为支持TrueType和OpenType字体(以及FreeType库支持的其他字体格式)。

"""

from PIL import Image, ImageFont, ImageDraw

img01 = Image.open("b.jpeg")

# 需求： 在图像上绘制文字   -- 必须掌握
# 绘制文字需要使用ImageDraw和ImageFont模块
# ImageFont的作用是进行绘制的
# ImageFont的作用是设置字体的

# 加载字体文件，创建font对象
# 默认在操作系统的字体文件中查找
try:
    font = ImageFont.truetype("simhei.ttf", size=50)
except OSError:
    font = ImageFont.load_default(size=50)
# 1. 通过image图像对象得到画笔Draw对象
draw = ImageDraw.Draw(img01)
# 2. 绘制文字
# fill: 文字填充的颜色
draw.text((100, 100), "我爱你", fill=(255, 0, 0), font=font)
img01.show()

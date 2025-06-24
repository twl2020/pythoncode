"""
ImageEnhance模块：包含许多可用于图像增强的类。
PIL.ImageEnhance.Color(image)：这个类可以用来调整图像的色彩平衡，类似于彩色电视机上的控件。增强系数为0.0会得到黑白图像。系数为1.0的是原始图像。
PIL.ImageEnhance.Contrast(image)：该类可用于控制图像的对比度，类似于电视机上的对比度控制。增强系数为0.0会得到纯灰色图像，系数为1.0会得到原始图像，更大的值会增加图像的对比度。
PIL.ImageEnhance.Brightness(image)：这个类可以用来控制图像的亮度。增强系数为0.0的图像为黑色，系数为1.0的图像为原始图像，更大的值会增加图像的亮度。
PIL.ImageEnhance.Sharpness(image)：此类可用于调整图像的清晰度。增强系数为0.0的图像是模糊的，系数为1.0的图像是原始图像，系数为2.0的图像是锐化的。


enhance(factor)：返回增强图像。
factor -控制增强的浮点值。因子1.0总是返回原始图像的副本，
因子越低意味着颜色越少(亮度、对比度等)，而值越高则越多。这个值没有限制。

"""
from PIL import Image, ImageEnhance

img01 = Image.open("b.jpeg")

# img02 = ImageEnhance.Color(img01).enhance(0.5)
# img02 = ImageEnhance.Contrast(img01).enhance(0.5)
# img02 = ImageEnhance.Brightness(img01).enhance(0.9)
img02 = ImageEnhance.Sharpness(img01).enhance(100)
img02.show()


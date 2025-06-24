"""
PIL.Image.blend(im1: Image, im2: Image, alpha: float) → Image: 图像混合，通过在两个输入图像之间插值创建一个新图像，使用常数alpha:
out = image1 * (1.0 - alpha) + image2 * alpha
第二张图。必须具有与第一张图像相同的模式和大小。
alpha插值因子。如果alpha为0.0，则返回第一张图像的副本。
如果alpha为1.0，则返回第二个图像的副本。对alpha值没有限制。如果需要，结果将被裁剪以适应允许的输出范围。



PIL.Image.eval(image, fun) -> Image:
将函数(应该有一个参数)应用于给定图像中的每个像素。如果图像有多个通道，则对每个通道应用相同的函数。
请注意，该函数对每个可能的像素值求值一次，因此不能使用随机组件或其他生成器。

"""
from PIL import Image

img01 = Image.open("b.jpeg")
img02 = Image.open("mn.jpeg").resize(size=(720, 1280))

# 图像混合
img3 = Image.blend(img01, img02, 0.1)
img3.show()

# 将图像中每个像素值增加100
img4 = Image.eval(img01, lambda p: p + 100)
img4.show()






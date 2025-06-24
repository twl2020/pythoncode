"""
Image.transpose(method: Transpose) → Image：转置图像(以90度的步骤翻转或旋转)
method 参数决定了图片要如何翻转，参数值如下：
Image.Transpose.FLIP_LEFT_RIGHT：左右水平翻转；
Image.Transpose.FLIP_TOP_BOTTOM：上下垂直翻转；
Image.Transpose.ROTATE_90：图像旋转 90 度；
Image.Transpose.ROTATE_180：图像旋转 180 度；
Image.Transpose.ROTATE_270：图像旋转 270 度；
Image.Transpose.TRANSPOSE：图像转置；
Image.Transpose.TRANSVERSE：图像横向翻转。

"""
from PIL import Image

img = Image.open("b.jpeg")

img1 = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img1.show()
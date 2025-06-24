"""
Image.resize(size, resample=None, box=None) → Image：返回此图像调整大小后的副本。
Size: 以像素为单位的大小，作为一个2元组:(width, height)。
Resample: 可选参数，指图像重采样滤波器，有四种过滤方式，分别是
Image.BICUBIC（双立方插值法）、
PIL.Image.NEAREST（最近邻插值法）、
PIL.Image.BILINEAR（双线性插值法）、
PIL.Image.LANCZOS（下采样过滤插值法），
如果图像的模式为“1”或“P”，则始终设置为Resampling.NEAREST。默认为 Image.BICUBIC
Box: 对指定图片区域进行缩放，box 的参数值是长度为 4 的像素坐标元组，即 (左,上,右,下)。
注意，被指定的区域必须在原图的范围内，如果超出范围就会报错。当不传该参数时，默认对整个原图进行缩放；

"""
from PIL import Image

img = Image.open("b.jpeg")
img1 = img.resize(size=(1440, 2560), resample=Image.Resampling.BICUBIC, box=(100, 100, 300, 500))
img1.show()




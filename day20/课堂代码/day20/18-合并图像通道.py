"""
PIL.Image.merge(mode, bands) ->Image: 合并一组单通道图像到一个新的多通道图像。
mode - 用于输出图像的模式
Bands – 需要合并的单通道图像序列，所有图像必须具有相同的大小

"""

from PIL import Image

img01 = Image.open("b.jpeg")
r, g, b = img01.split()
img02 = Image.merge("RGB", bands=(b, g, r))
img02.show()

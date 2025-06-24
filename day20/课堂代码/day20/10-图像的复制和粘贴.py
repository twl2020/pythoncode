"""
Image.copy() → Image 复制此图像。如果您希望将内容粘贴到图像中，但仍保留原始图像，则使用此方法。

Image.paste(im, box=None, mask=None) → None:将另一个图像粘贴到此图像中。
box参数要么是一个给出左上角的2元组，要么是一个定义左、上、右和下像素坐标的4元组，要
么是None(与(0,0)相同)。参见坐标系统。如果给出了一个4元组，则粘贴图像的大小必须与区域的大小匹配。
如果模式不匹配，则将粘贴的图像转换为该图像的模式
源可以是包含像素值的整数或元组，而不是图像。然后该方法用给定的颜色填充该区域。


"""
from PIL import Image

img1 = Image.open("b.jpeg")
img2 = Image.open("mn.jpeg")

# 复制
img3 = img1.copy()

# 将img2粘贴到img3上
# 没有指定box, 表示从左上角开始站粘贴
# img3.paste(img2)
# box=(100, 100) 指定的是左上角的坐标
# img3.paste(img2, box=(100, 100))
# 如果给出了一个4元组，则粘贴图像的大小必须与区域的大小匹配。
img3.paste(img2, box=(100, 100, 740, 840))
img3.show()



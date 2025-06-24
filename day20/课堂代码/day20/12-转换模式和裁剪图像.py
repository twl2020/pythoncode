from PIL import Image
"""
Image.convert(mode: str) → Image : 返回此图像的转换副本。
Image.crop(box: tuple[int, int, int, int]) → Image: 以矩形区域的方式对原图像进行裁剪。
该框是一个4元组，定义了左、上、右和下像素坐标(参见坐标系统)。默认box = None 表示拷贝原图像。

"""
img = Image.open("b.jpeg")

print(img.mode)

# 转换图像的模式
img1 = img.convert(mode="L")
# img1.show()

# 裁剪图像
img2 = img.crop((10, 30, 500, 500))
img2.show()


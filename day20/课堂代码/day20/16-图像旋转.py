"""
Image.rotate(angle, resample=Resampling.NEAREST, expand=0, center=None, translate=None, fillcolor=None)：返回此图像的旋转副本。此方法返回该图像的副本，并围绕其中心逆时针旋转给定的度数。
    angle：以逆时针方向为单位。
    expand：可选的扩展标志。如果为true，则扩展输出图像，使其足够大以容纳整个旋转图像。如果为false或省略，则使输出图像与输入图像大小相同。注意，扩展标志假设围绕中心旋转，而不是平移。
    center: 可选的旋转中心(一个2元组)。原点在左上角。默认是图像的中心。
    translate: 可选的，表示旋转后平移(一个2元组)。
    fillcolor：可选的，旋转图像外区域的填充颜色。
"""
from PIL import Image

img = Image.open("b.jpeg")
# img1 = img.rotate(20, expand=True)
# img1 = img.rotate(20, translate=(100, 200))
img1 = img.rotate(20, fillcolor=(255, 0, 0))
# img1.show()

# 保存旋转后的图像
img1.save("img1.png")
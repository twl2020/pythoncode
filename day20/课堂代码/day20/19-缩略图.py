"""
Image.thumbnail(size, resample=Resampling.BICUBIC) -> None： 生成指定大小的缩略图
"""
from PIL import Image

img01 = Image.open("b.jpeg")

# 会按照最大的尺寸进行等比缩放
# 缩略图是做缩小
img01.thumbnail(size=(300, 300))
img01.show()


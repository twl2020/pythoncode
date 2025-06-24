import numpy as np
from PIL import Image

img = Image.new(mode="RGB", size=(2, 4), color=(255, 0, 0))

# 将Image转成numpy
arr = np.array(img)
# print(arr)
# Pillow中图像的形状默认是 HWC的形状
# print(arr.shape)  # 形状(6, 4, 3)
# HWC -- CHW
arr01 = np.transpose(arr, (2, 0, 1))
print(arr01)

print("---------------------------------------")

# 将numpy转成Image
# shape(0轴， 1轴)  表示的高度和宽度
# 以后只要是numpy数组转图像， 先做第一件事： 将数据类型变成 uint8
arr = np.zeros((640, 480), dtype="u1")
arr[100:300, 100: 300] = [255, 0, 0]
print(arr.dtype)  # float64
# img = Image.fromarray(arr, "L")
# Pillow不支持每通道深度超过8位的多通道图像。
img = Image.fromarray(arr, "RGB")
img.show()

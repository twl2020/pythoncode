from PIL import Image
"""
Image.getbands(): 返回图像中每个通道名称的元组。例如，RGB图像上的getbands返回(“R”，“G”，“B”)。
image.getchannel(channel): 返回图像的单个通道的图像。
channel -返回哪个通道。可以是索引(“RGB”的“R”通道为0)或通道名称(“RGBA”的alpha通道为“A”)。

"""
img = Image.open("rgb.png")

# 获取通道的名称
t = img.getbands()
print(t)

# 根据通道的名称获取指定通道的图像
r_img = img.getchannel("B")
r_img.show()
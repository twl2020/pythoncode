from PIL import Image

img = Image.open("c.jpeg")
# 获取图像的宽高
w, h = img.size

# 将图像拆分四等分
im01 = img.crop(box=(0, 0, w // 2, h // 2))
im02 = img.crop(box=(w // 2, 0, w, h // 2))
im03 = img.crop(box=(0, h // 2, w // 2, h))
im04 = img.crop(box=(w // 2, h // 2, w, h))

# 将以上拆分出来的图像再合并成图像
# 创建一张新的背景图
img_new = Image.new("RGB", size=(w, h))
# 将图像粘贴到背景图上
img_new.paste(im01, box=(0, 0))
img_new.paste(im02, box=(w // 2, 0))
img_new.paste(im03, box=(0, h // 2))
img_new.paste(im04, box=(w // 2, h // 2))
img_new.show()

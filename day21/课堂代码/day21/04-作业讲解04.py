from PIL import Image

img = Image.open("c.jpeg")
# 获取图像的宽高
w, h = img.size

# 将图像拆分四等分
rows = 2
cols = 2
# 存储拆分的小图像
img_list = []
for i in range(rows):
    for j in range(cols):
        im = img.crop(box=(w // 2 * j, h // 2 * i, w // 2 * (j + 1), h // 2 * (i + 1)))
        img_list.append(im)

# 将以上拆分出来的图像再合并成图像
# 创建一张新的背景图
img_new = Image.new("RGB", size=(w, h))
# 将图像粘贴到背景图上
for i in range(rows):
    for j in range(cols):
        img_new.paste(img_list[i * 2 + j], box=(w // 2 * j, h // 2 * i))
img_new.show()

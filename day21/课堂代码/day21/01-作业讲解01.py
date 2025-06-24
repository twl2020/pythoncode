"""生成随机码"""
from PIL import Image, ImageFont, ImageDraw
import random, string


def get_random_color():
    return random.randint(0, 255)


# 1. 生成随机的字母和数字
str = string.ascii_letters + string.digits
code_list = random.choices(str, k=4)

# 2. 生成背景图
bg = Image.new("RGB", size=(400, 150))
# 3. 绘制文字
# 3.1 创建font对象
font = ImageFont.load_default(70)
# 3.2 根据图像获取到画笔
draw = ImageDraw.Draw(bg)
# 3.3 绘制文字， 文字需要一个一个的循环绘制， 因为每个颜色不一样
for i, code in enumerate(code_list):
    draw.text((50 + (i * 70), 20), code, fill=(get_random_color(), get_random_color(), get_random_color()), font=font)
bg.show()
